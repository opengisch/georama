import uuid
from operator import attrgetter

from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.http import FileResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from qgis_server_light.interface.job.common.input import ExecutionMode
from qgis_server_light.interface.job.process.description import ProcessDescriptions
from qgis_server_light.interface.job.process.input import (
    OutputFormat,
    QslJobParameterExecuteProcess,
)
from rest_framework import filters, renderers, status
from rest_framework.decorators import action
from rest_framework.exceptions import (
    NotAcceptable,
    NotFound,
    PermissionDenied,
    ValidationError,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.core.common.api import (
    GeoramaManagerViewSet,
    GeoramaManagerWithPermissionsViewSet,
    GeoramaModelPermissions,
    GeoramaObjPermViewSetReadOnly,
)
from georama.core.common.menu import ActionType, Breadcrumb, BreadcrumbAction
from georama.core.common.request import GeoramaDrfRequest
from georama.integration.models import Datasource
from georama.processes.adapter import qsl
from georama.processes.api.serializers import (
    JobSerializer,
    ProcessInputObjectPermissionSerializer,
    ProcessInputPermissionActionSerializer,
    ProcessInputSerializer,
    ProcessObjectPermissionSerializer,
    ProcessPermissionActionSerializer,
    ProcessSerializer,
    PublishFromDatasourceInput,
)
from georama.processes.interface.ogc_api.processes.part1.v_100.main import (
    Conformance,
    ExceptionDocument,
    ExceptionType,
    Jobs,
    Landing,
    Link,
    Processes,
    StatusCode,
)
from georama.processes.interface.ogc_api.processes.part1.v_100.serializers import (
    OgcApiDictEncoder,
    OgcApiProcessDetailDictEncoder,
)
from georama.processes.mappers.layer_inputs import LayerInputMapper
from georama.processes.models.job import Job
from georama.processes.models.process import Process
from georama.processes.models.process_input import ProcessInput
from georama.processes.processes_config import Config

User = get_user_model()


class LandingView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "processes/drf/landing.html"

    def get(self, request, *args, **kwargs):
        context = {
            "view": self,
            "breadcrumbs": [
                Breadcrumb("Processes"),
            ],
            "object": Landing(
                title="Georama OGC API Processes",
                description="...",
                links=[
                    Link(
                        type="application/json",
                        rel="self",
                        href=f"{request.build_absolute_uri(reverse('processes:api-landing'))}?f=json",
                        href_lang="en",
                        title=_("This document as JSON"),
                    ),
                    Link(
                        type="text/html",
                        rel="self",
                        href=f"{request.build_absolute_uri(reverse('processes:api-landing'))}?f=html",
                        href_lang="en",
                        title=_("This document as HTML"),
                    ),
                    Link(
                        type="application/json",
                        rel="conformance",
                        href=request.build_absolute_uri(reverse("processes:api-conformance")),
                        href_lang="en",
                        title=_("Conformance"),
                    ),
                    Link(
                        type="application/json",
                        rel="http://www.opengis.net/def/rel/ogc/1.0/processes",
                        href=request.build_absolute_uri(reverse("processes:process-list")),
                        href_lang="en",
                        title=_("Process list"),
                    ),
                    Link(
                        type="application/json",
                        rel="http://www.opengis.net/def/rel/ogc/1.0/job-list",
                        href=request.build_absolute_uri(reverse("processes:job-list")),
                        href_lang="en",
                        title=_("Jobs list"),
                    ),
                ],
            ),
        }
        if request.accepted_renderer.format == "html":
            return Response(context, template_name=self.template_name)

        return Response(OgcApiDictEncoder().encode(context["object"]))


class ConformanceView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "processes/drf/conformance.html"

    def get(self, request, *args, **kwargs):
        context = {
            "view": self,
            "breadcrumbs": [
                Breadcrumb("Processes", reverse("processes:api-landing")),
                Breadcrumb("Conformance"),
            ],
            "object": Conformance(
                conforms_to=[
                    "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core",
                    "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/ogc-process-description",
                    "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/json",
                    "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/job-list",
                ]
            ),
        }
        if request.accepted_renderer.format == "html":
            return Response(context, template_name=self.template_name)

        return Response(OgcApiDictEncoder().encode(context["object"]))


class ProcessDescriptionMixin:
    async def aprepare_page(self, page) -> list[Process]:
        return await page.adescribed()

    async def aget_object(self):
        process = await super().aget_object()
        process.process_description = await qsl.process_description(process.algorithm_id)
        return process


class ProcessInputDescriptionMixin(ProcessDescriptionMixin):
    process_input_perms = ["processes.use_as_process_input"]

    async def aprepare_page(self, page) -> list[Process]:
        processes = await super().aprepare_page(page)
        await self.amap_layer_inputs(processes)
        return processes

    async def aget_object(self):
        process = await super().aget_object()
        await self.amap_layer_inputs([process])
        return process

    async def alayer_input_mapper(self) -> LayerInputMapper:
        return LayerInputMapper(await self.aaccessible_process_inputs())

    async def amap_layer_inputs(self, processes: list[Process]):
        layer_input_mapper = await self.alayer_input_mapper()
        for process in processes:
            if process.process_description is not None:
                process.process_description = layer_input_mapper.map_process_description(
                    process.process_description
                )

    async def aaccessible_process_inputs(self) -> list[ProcessInput]:
        queryset = await sync_to_async(ProcessInput.objects.accessible_objects)(
            self.request.georama_organisation,
            self.request.user,
            self.process_input_perms,
            include_public=True,
        )
        return [process_input async for process_input in queryset]


class ManageProcessViewSet(ProcessDescriptionMixin, GeoramaManagerWithPermissionsViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["algorithm_id"]
    ordering_fields = ["algorithm_id"]
    filterset_fields = []
    algorithm_attribute_by_ordering_field = {"algorithm_id": "id"}

    permissions_serializer_class = ProcessObjectPermissionSerializer
    permissions_action_serializer_class = ProcessPermissionActionSerializer

    list_body_partial_template_name: str = "processes/drf/process/partials/list_body.html"
    list_body_unpublished_partial_template_name: str = (
        "processes/drf/process/partials/list_body_unpublished.html"
    )
    show_template_name = "processes/drf/process/detail.html"
    process_descriptions: ProcessDescriptions | None = None

    async def get_breadcrumbs(self):
        breadcrumbs = await super().get_breadcrumbs()
        breadcrumbs[0].view_name = reverse("processes:api-landing")
        return breadcrumbs

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["process_descriptions"] = self.process_descriptions
        return context

    async def acreate(self, request: GeoramaDrfRequest, *args, **kwargs):
        self.process_descriptions = await qsl.process_descriptions()
        response = await super().acreate(request, *args, **kwargs)
        if request.accepted_renderer.format == "html":
            return redirect(reverse(self.url_name_list))
        return response

    async def perform_acreate(self, serializer):
        await serializer.asave(organisation=self.request.georama_organisation)
        serializer.instance.process_description = await qsl.process_description(
            serializer.instance.algorithm_id
        )

    @property
    async def bread_crumb_action_context(self):
        """Prepares the breadcrumb action to add a project.

        Returns:
            The context with an action to add a new project in case the user has either
            add, delete or change permission or is admin user.
        """
        context = {}
        model_perms = await self._get_model_permissions()
        url_action_target = reverse(self.non_published_url_name)
        if (
            any(model_perms.values()) or self.request.user.is_superuser
        ) and self.request.path != url_action_target:
            context["breadcrumb_action"] = BreadcrumbAction(
                url=url_action_target,
                tooltip=_("Publish processes from QGIS"),
                hint=_("Select a process to publish"),
                title=_("Process"),
                type=ActionType.LINKED,
                icon="fa fa-circle-plus",
            )
        return context

    @property
    def non_published_url_name(self):
        return self.url_name("non-published")

    @action(detail=False, methods=["get"], url_path="non_published")
    async def non_published(self, request: GeoramaDrfRequest, *args, **kwargs):
        published_algorithm_ids = set(
            await sync_to_async(list)(self.get_queryset().values_list("algorithm_id", flat=True))
        )

        search = request.query_params.get("search", "")
        process_descriptions = await qsl.process_descriptions()
        algorithms = qsl.non_published_process_descriptions(
            process_descriptions, published_algorithm_ids, search
        )
        ordering_filter = filters.OrderingFilter()
        ordering = ordering_filter.get_ordering(request, algorithms, self) or []
        for ordering_field in reversed(ordering):
            algorithms.sort(
                key=attrgetter(
                    self.algorithm_attribute_by_ordering_field[ordering_field.removeprefix("-")]
                ),
                reverse=ordering_field.startswith("-"),
            )
        # the page holds process descriptions and no processes, so it is not described
        pqs = await self.paginator.paginate_queryset(algorithms, request, view=self)

        if request.accepted_renderer.format == "html":
            context = await super()._prepare_many_context()
            context["breadcrumbs"][-1].view_name = self.reverse_action("list")
            context["breadcrumbs"].append(Breadcrumb(_("Non published processes")))
            # context["organisation"] = organisation_folder
            context["object_list"] = pqs
            context["process_registry_empty"] = not process_descriptions.processes
            context["limit"] = self.paginator.limit
            context["list_body_partial"] = self.list_body_unpublished_partial_template_name
            context["ordering_context"] = self.build_ordering_context(
                request=request,
                queryset=algorithms,
                ordering_filter=ordering_filter,
            )
            context.update(await self._get_model_permissions())
            context.update(self.paginator.get_html_context())
            if request.META.get("HTTP_HX_REQUEST") == "true":
                template_name = self.list_partial_template_name
            else:
                template_name = self.list_template_name
            return Response(context, template_name=template_name)


class ProcessViewSet(ProcessInputDescriptionMixin, GeoramaObjPermViewSetReadOnly):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    required_obj_perms = [
        "processes.execute_process",
    ]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["algorithm_id"]
    ordering_fields = ["algorithm_id"]
    filterset_fields = []

    list_body_partial_template_name: str = "processes/drf/process/partials/list_body.html"
    show_template_name = "processes/drf/process/detail.html"
    execute_template_name = "processes/drf/process/execution.html"
    output_form_prefix = "outputs"

    async def get_breadcrumbs(self):
        breadcrumbs = await super().get_breadcrumbs()
        breadcrumbs[0].view_name = reverse("processes:api-landing")
        return breadcrumbs

    async def afilter_queryset(self, queryset):
        queryset = await super().afilter_queryset(queryset)
        return queryset.filter(algorithm_id__in=await qsl.served_algorithm_ids())

    async def alist(self, request: GeoramaDrfRequest, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            return await super().alist(request, *args, **kwargs)

        queryset = await self.afilter_queryset(self.get_queryset())
        page = await self.apaginate_queryset(queryset)
        processes = [
            process.dataclass
            for process in await self.aprepare_page(page if page is not None else queryset)
        ]

        links = [
            Link(
                rel="self",
                title="Processes (current page)",
                href=request.build_absolute_uri(),
                type="application/json",
            )
        ]
        paginator = self.paginator
        if page is not None and paginator is not None:
            if next_link := paginator.get_next_link():
                links.append(
                    Link(
                        rel="next",
                        title="Processes (next page)",
                        href=next_link,
                        type="application/json",
                    )
                )
            if previous_link := paginator.get_previous_link():
                links.append(
                    Link(
                        rel="prev",
                        title="Processes (previous page)",
                        href=previous_link,
                        type="application/json",
                    )
                )

        return Response(OgcApiDictEncoder().encode(Processes(processes=processes, links=links)))

    async def aretrieve(self, request: GeoramaDrfRequest, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            return await super().aretrieve(request, *args, **kwargs)

        process = await self.aget_object()
        return Response(OgcApiProcessDetailDictEncoder().encode(process.detail_dataclass))

    @action(detail=True, methods=["get", "post"], url_name="execution", url_path="execution")
    async def execution(self, request: GeoramaDrfRequest, *args, **kwargs):
        context = await self._prepare_single_context()
        context["form"] = context["object"].inputs_html_form
        context["output_form"] = context["object"].outputs_html_form(prefix=self.output_form_prefix)
        if request.method == "GET":
            if request.accepted_renderer.format == "html":
                return Response(context, template_name=self.execute_template_name)
            else:
                raise NotAcceptable("This endpoint GET method only supports HTML.")

        is_html = request.accepted_renderer.format == "html"
        if is_html:
            form = context["form"](request.POST)
            output_form = context["object"].outputs_html_form(
                request.POST, prefix=self.output_form_prefix
            )
        else:
            inputs = request.data.get("inputs")
            if not isinstance(inputs, dict):
                raise ValidationError({"inputs": _("Expected an object of process inputs.")})
            form = context["form"](data=inputs)
            output_form = context["object"].outputs_html_form(
                data=self.media_type_by_output_id(request.data.get("outputs", {}))
            )
            if unknown_output_ids := set(output_form.data) - set(output_form.fields):
                raise ValidationError(
                    {"outputs": _("Unknown outputs: %s") % ", ".join(sorted(unknown_output_ids))}
                )

        inputs_valid = form.is_valid()
        outputs_valid = output_form.is_valid()
        if not (inputs_valid and outputs_valid):
            if is_html:
                context["form"] = form
                context["output_form"] = output_form
                return Response(context, template_name=self.execute_template_name, status=400)
            errors = dict(form.errors)
            if output_form.errors:
                errors["outputs"] = output_form.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        process: Process = context["object"]
        # the layer markers are only in the unmapped description, so it is fetched again
        layer_input_mapper = await self.alayer_input_mapper()
        parameters = await layer_input_mapper.amap_parameter_inputs(
            await qsl.process_description(process.algorithm_id),
            form.cleaned_data,
        )
        output_formats = [
            OutputFormat(name=name, media_type=media_type)
            for name, media_type in output_form.cleaned_data.items()
            if media_type
        ]
        created_at = timezone.now()
        # Georama runs in autocommit, the row is committed when `acreate` returns. So the
        # job is only submitted afterwards and a worker never sees a job without its row.
        job = await Job.objects.acreate(
            redis_job_id=uuid.uuid4(),
            created_by=request.user,
            created_at=created_at,
            expires=created_at + Config().job_expire,
            process=process,
            job_parameters=DictEncoder().encode(parameters),
        )
        job_parameter = QslJobParameterExecuteProcess(
            process_id=process.algorithm_id,
            parameters=parameters,
            output_formats=output_formats,
        )

        if is_html:
            await qsl.submit_job(str(job.redis_job_id), job_parameter)
            return redirect(reverse("processes:job-detail", kwargs={"pk": job.pk}))
        if self.prefers_async(request):
            await qsl.submit_job(str(job.redis_job_id), job_parameter)
            return self.job_status_response(
                request, job, headers={"Preference-Applied": "respond-async"}
            )
        await qsl.submit_job(str(job.redis_job_id), job_parameter, ExecutionMode.SYNC)
        job.apply_state(await qsl.wait_for_job(str(job.redis_job_id)))
        await job.asave()
        if job.status == StatusCode.SUCCESSFUL:
            return Response(job.results(request.build_absolute_uri), status=status.HTTP_200_OK)
        if job.status == StatusCode.FAILED:
            return Response(
                OgcApiDictEncoder().encode(job.status_info(request.build_absolute_uri)),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        # the job did not finish in time, the client continues as if it asked for async
        return self.job_status_response(request, job)

    @staticmethod
    def media_type_by_output_id(outputs) -> dict[str, str]:
        if not isinstance(outputs, dict):
            raise ValidationError({"outputs": _("Expected an object of process outputs.")})
        try:
            return {
                output_id: output["format"]["mediaType"]
                for output_id, output in outputs.items()
                if "format" in output
            }
        except (KeyError, TypeError) as e:
            raise ValidationError(
                {"outputs": _("Expected format.mediaType for each output with a format.")}
            ) from e

    @staticmethod
    def prefers_async(request: GeoramaDrfRequest) -> bool:
        return "respond-async" in request.headers.get("Prefer", "")

    @staticmethod
    def job_status_response(
        request: GeoramaDrfRequest, job: Job, headers: dict | None = None
    ) -> Response:
        return Response(
            OgcApiDictEncoder().encode(job.status_info(request.build_absolute_uri)),
            status=status.HTTP_201_CREATED,
            headers={
                "Location": request.build_absolute_uri(
                    reverse("processes:job-detail", kwargs={"pk": job.pk})
                ),
                **(headers or {}),
            },
        )


class ManageProcessInputViewSet(GeoramaManagerWithPermissionsViewSet):
    queryset = ProcessInput.objects.all()
    serializer_class = ProcessInputSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["datasource__name"]
    ordering_fields = ["datasource__name", "public"]
    filterset_fields = []
    list_body_partial_template_name = "processes/drf/process_input/partials/list_body.html"

    permissions_serializer_class = ProcessInputObjectPermissionSerializer
    permissions_action_serializer_class = ProcessInputPermissionActionSerializer

    async def get_breadcrumbs(self):
        breadcrumbs = await super().get_breadcrumbs()
        breadcrumbs[0].view_name = reverse("processes:api-landing")
        return breadcrumbs

    @property
    async def bread_crumb_action_context(self):
        """Prepares the breadcrumb action to publish a datasource as process input.

        Returns:
            The context with an action to publish a datasource in case the user has
            add-permission on the process input model and is permitted to view datasources.
        """
        context = {}

        perm_checker = GeoramaModelPermissions()
        # post is the DRF method which is used for add/create a new object
        local_perms = perm_checker.get_required_permissions("POST", self.queryset.model)
        # we also check if the remote data can be used (view)
        remote_perms = perm_checker.get_required_permissions("GET", Datasource)
        if all(
            [
                await self.request.user.ahas_perms(local_perms),
                await self.request.user.ahas_perms(remote_perms),
            ]
        ):
            context["breadcrumb_action"] = BreadcrumbAction(
                url=reverse("integration:manager-datasource-list"),
                tooltip=_("Publish a Datasource as process input"),
                hint=_("Select a Datasource to publish it as a new process input"),
                title=_("Process input"),
                type=ActionType.EMBEDDED,
                icon="fa fa-circle-plus",
            )
        return context

    @extend_schema(
        description="Publishes a datasource as process input, meaning, processes can be "
        "executed with it as layer input. Publishing a datasource twice keeps the existing "
        "process input.",
        request=PublishFromDatasourceInput,
    )
    @action(detail=False, methods=["post"], url_path="publish_from_datasource")
    async def publish_from_datasource(self, request: GeoramaDrfRequest, *args, **kwargs):
        perms = await self._get_model_permissions()
        if perms["can_add"]:
            pfdi = PublishFromDatasourceInput(data=request.data)
            pfdi.is_valid(raise_exception=True)
            qs = Datasource.objects.organisation_objects(request.georama_organisation)
            datasource: Datasource = await qs.aget(id=pfdi.validated_data["pk"])
            await ProcessInput.objects.aget_or_create(datasource=datasource)
            return redirect(reverse(self.url_name_list))
        else:
            raise PermissionDenied()


class ProcessInputViewSet(GeoramaObjPermViewSetReadOnly):
    queryset = ProcessInput.objects.all()
    serializer_class = ProcessInputSerializer
    required_obj_perms = [
        "processes.use_as_process_input",
    ]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["datasource__name"]
    ordering_fields = ["datasource__name", "public"]
    filterset_fields = []
    list_body_partial_template_name = "processes/drf/process_input/partials/list_body.html"

    async def get_breadcrumbs(self):
        breadcrumbs = await super().get_breadcrumbs()
        breadcrumbs[0].view_name = reverse("processes:api-landing")
        return breadcrumbs


class ManageJobViewSet(GeoramaManagerViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    required_obj_perms = []
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = []
    ordering_fields = []
    filterset_fields = []

    list_body_partial_template_name: str = "processes/drf/job/partials/list_body.html"

    async def get_breadcrumbs(self):
        breadcrumbs = await super().get_breadcrumbs()
        breadcrumbs[0].view_name = reverse("processes:api-landing")
        return breadcrumbs


class JobViewSet(GeoramaObjPermViewSetReadOnly):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    required_obj_perms = []
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = []
    ordering_fields = []
    filterset_fields = []

    list_body_partial_template_name: str = "processes/drf/job/partials/list_body.html"
    show_template_name: str = "processes/drf/job/detail.html"

    async def get_breadcrumbs(self):
        breadcrumbs = await super().get_breadcrumbs()
        breadcrumbs[0].view_name = reverse("processes:api-landing")
        return breadcrumbs

    async def public_or_object_permission(self, queryset):
        # jobs are neither public nor have object permissions, they belong to their issuer
        if self.request.user.is_superuser:
            return queryset
        if self.request.user.is_authenticated:
            return queryset.filter(created_by=self.request.user)
        return queryset.none()

    async def aprepare_page(self, page) -> list[Job]:
        jobs = [job async for job in page]
        for job in jobs:
            await self.arefresh_state(job)
        return jobs

    async def aget_object(self):
        job = await super().aget_object()
        await self.arefresh_state(job)
        return job

    @staticmethod
    async def arefresh_state(job: Job):
        # lazy sync, finished jobs don't change anymore
        if job.is_finished:
            return
        job.apply_state(await qsl.job_state(str(job.redis_job_id)))
        await job.asave()

    async def alist(self, request: GeoramaDrfRequest, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            return await super().alist(request, *args, **kwargs)

        queryset = await self.afilter_queryset(self.get_queryset())
        page = await self.apaginate_queryset(queryset)
        jobs = [
            job.status_info(request.build_absolute_uri)
            for job in await self.aprepare_page(page if page is not None else queryset)
        ]

        links = [
            Link(
                rel="self",
                title="Jobs (current page)",
                href=request.build_absolute_uri(),
                type="application/json",
            )
        ]
        paginator = self.paginator
        if page is not None and paginator is not None:
            if next_link := paginator.get_next_link():
                links.append(
                    Link(
                        rel="next",
                        title="Jobs (next page)",
                        href=next_link,
                        type="application/json",
                    )
                )
            if previous_link := paginator.get_previous_link():
                links.append(
                    Link(
                        rel="prev",
                        title="Jobs (previous page)",
                        href=previous_link,
                        type="application/json",
                    )
                )
        return Response(OgcApiDictEncoder().encode(Jobs(jobs=jobs, links=links)))

    async def aretrieve(self, request: GeoramaDrfRequest, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            return await super().aretrieve(request, *args, **kwargs)

        job = await self.aget_object()
        return Response(OgcApiDictEncoder().encode(job.status_info(request.build_absolute_uri)))

    @action(detail=True, methods=["get"], url_name="results")
    async def results(self, request: GeoramaDrfRequest, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            # the job page shows the results next to the status
            return await self.aretrieve(request, *args, **kwargs)

        job = await self.aget_object()
        if job.status == StatusCode.SUCCESSFUL:
            return Response(job.results(request.build_absolute_uri))
        if job.status in (StatusCode.FAILED, StatusCode.DISMISSED):
            return self.exception_response(
                ExceptionType.JOB_RESULTS_FAILED,
                _("The job did not succeed, it has no results."),
                job.message,
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return self.exception_response(
            ExceptionType.RESULT_NOT_READY,
            _("The job is not finished yet."),
            job.message,
            status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=True,
        methods=["get"],
        url_name="output",
        url_path=r"results/(?P<output_name>[^/]+)",
    )
    async def output(self, request: GeoramaDrfRequest, output_name: str, *args, **kwargs):
        job = await self.aget_object()
        file_output = job.file_output(output_name)
        if file_output is None:
            raise NotFound(_("The job has no file output %s.") % output_name)
        path = job.file_output_path(file_output)
        if path is None or not path.is_file():
            raise NotFound(_("The file of output %s is not available.") % output_name)
        return FileResponse(
            path.open("rb"),
            as_attachment=True,
            filename=path.name,
            content_type=file_output.media_type,
        )

    @staticmethod
    def exception_response(
        exception_type: ExceptionType, title: str, detail: str | None, status_code: int
    ) -> Response:
        return Response(
            OgcApiDictEncoder().encode(
                ExceptionDocument(
                    type=exception_type, title=title, status=status_code, detail=detail
                )
            ),
            status=status_code,
        )
