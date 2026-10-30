import uuid
from operator import attrgetter

from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from qgis_server_light.interface.job.process.input import (
    ParameterInput,
    QslJobParameterExecuteProcess,
)
from rest_framework import filters, renderers, status
from rest_framework.decorators import action
from rest_framework.exceptions import NotAcceptable, ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.core.common.api import (
    GeoramaManagerViewSet,
    GeoramaManagerWithPermissionsViewSet,
    GeoramaObjPermViewSetReadOnly,
)
from georama.core.common.menu import ActionType, Breadcrumb, BreadcrumbAction
from georama.core.common.request import GeoramaDrfRequest
from georama.processes.api.serializers import (
    JobSerializer,
    ProcessObjectPermissionSerializer,
    ProcessPermissionActionSerializer,
    ProcessSerializer,
)
from georama.processes.apps import qsl_available_processes, qsl_redis_queue
from georama.processes.interface.ogc_api.processes.part1.v_100.main import (
    Conformance,
    Jobs,
    Landing,
    Link,
    Processes,
)
from georama.processes.models.job import Job
from georama.processes.models.process import Process

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

        return Response(DictEncoder().encode(context["object"]))


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
                ]
            ),
        }
        if request.accepted_renderer.format == "html":
            return Response(context, template_name=self.template_name)

        return Response(DictEncoder().encode(context["object"]))


class ManageProcessViewSet(GeoramaManagerWithPermissionsViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["id"]
    ordering_fields = ["id"]
    filterset_fields = []

    permissions_serializer_class = ProcessObjectPermissionSerializer
    permissions_action_serializer_class = ProcessPermissionActionSerializer

    list_body_partial_template_name: str = "processes/drf/process/partials/list_body.html"
    list_body_unpublished_partial_template_name: str = (
        "processes/drf/process/partials/list_body_unpublished.html"
    )
    show_template_name = "processes/drf/process/detail.html"

    async def get_breadcrumbs(self):
        breadcrumbs = await super().get_breadcrumbs()
        breadcrumbs[0].view_name = reverse("processes:api-landing")
        return breadcrumbs

    async def acreate(self, request: GeoramaDrfRequest, *args, **kwargs):
        response = await super().acreate(request, *args, **kwargs)
        if request.accepted_renderer.format == "html":
            return redirect(reverse(self.url_name_list))
        return response

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
        published_process_ids = set(
            await sync_to_async(list)(Process.objects.values_list("id", flat=True))
        )

        search = request.query_params.get("search", "")
        algorithms = [
            algorithm
            for algorithm in qsl_available_processes.algorithms
            if algorithm.id not in published_process_ids
            and (not search or search in algorithm.name.lower())
        ]
        ordering_filter = filters.OrderingFilter()
        ordering = ordering_filter.get_ordering(request, algorithms, self) or []
        for ordering_field in reversed(ordering):
            algorithms.sort(
                key=attrgetter(ordering_field.removeprefix("-")),
                reverse=ordering_field.startswith("-"),
            )
        pqs = await self.apaginate_queryset(algorithms)

        if request.accepted_renderer.format == "html":
            context = await super()._prepare_many_context()
            context["breadcrumbs"][-1].view_name = self.reverse_action("list")
            context["breadcrumbs"].append(Breadcrumb(_("Non published processes")))
            # context["organisation"] = organisation_folder
            context["object_list"] = pqs
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


class ProcessViewSet(GeoramaObjPermViewSetReadOnly):
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
    search_fields = ["id"]
    ordering_fields = ["id"]
    filterset_fields = []

    list_body_partial_template_name: str = "processes/drf/process/partials/list_body.html"
    show_template_name = "processes/drf/process/detail.html"
    execute_template_name = "processes/drf/process/execution.html"

    async def get_breadcrumbs(self):
        breadcrumbs = await super().get_breadcrumbs()
        breadcrumbs[0].view_name = reverse("processes:api-landing")
        return breadcrumbs

    async def alist(self, request: GeoramaDrfRequest, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            return await super().alist(request, *args, **kwargs)

        queryset = await self.afilter_queryset(self.get_queryset())
        page = await self.apaginate_queryset(queryset)
        processes = []
        async for process in page if page is not None else queryset:
            processes.append(process.dataclass)

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

        return Response(DictEncoder().encode(Processes(processes=processes, links=links)))

    async def aretrieve(self, request: GeoramaDrfRequest, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            return await super().aretrieve(request, *args, **kwargs)

        process = await self.aget_object()
        return Response(DictEncoder().encode(process.dataclass))

    @action(detail=True, methods=["get", "post"], url_name="execution", url_path="execution")
    async def execution(self, request: GeoramaDrfRequest, *args, **kwargs):
        context = await self._prepare_single_context()
        context["form"] = context["object"].qsl_algorithm_params_html_form
        if request.method == "GET":
            if request.accepted_renderer.format == "html":
                return Response(context, template_name=self.execute_template_name)
            else:
                raise NotAcceptable("This endpoint GET method only supports HTML.")

        is_html = request.accepted_renderer.format == "html"
        if is_html:
            form = context["form"](request.POST)
        else:
            inputs = request.data.get("inputs")
            if not isinstance(inputs, dict):
                raise ValidationError({"inputs": _("Expected an object of process inputs.")})
            form = context["form"](data=inputs)

        if not form.is_valid():
            if is_html:
                context["form"] = form
                return Response(context, template_name=self.execute_template_name, status=400)
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

        parameters = [
            ParameterInput(name=name, value=value) for name, value in form.cleaned_data.items()
        ]
        job_parameters = QslJobParameterExecuteProcess(
            process_id=context["object"].pk,
            parameters=parameters,
        )
        job = await Job.objects.acreate(
            redis_job_id=uuid.uuid4(),
            created_by=request.user,
            created_at=timezone.now(),
            process=context["object"],
            job_parameters=DictEncoder().encode(parameters),
        )
        job_result, job_status = await qsl_redis_queue.post(job_parameters)
        job.redis_job_id = uuid.UUID(job_result.id)
        job.job_result = job_result.data
        await job.asave()

        if is_html:
            return redirect(reverse("processes:job-list"))
        return Response(
            DictEncoder().encode(job.dataclass),
            status=job_status.HTTP_201_CREATED,
            headers={
                "Location": request.build_absolute_uri(
                    reverse("processes:job-detail", kwargs={"pk": job.pk})
                )
            },
        )


class ManageJobViewSet(GeoramaManagerViewSet):
    queryset = Job.objects.all()
    serializer_class = ProcessSerializer
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

    async def get_breadcrumbs(self):
        breadcrumbs = await super().get_breadcrumbs()
        breadcrumbs[0].view_name = reverse("processes:api-landing")
        return breadcrumbs

    async def alist(self, request: GeoramaDrfRequest, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            return await super().alist(request, *args, **kwargs)

        queryset = await self.afilter_queryset(self.get_queryset())
        page = await self.apaginate_queryset(queryset)
        jobs = []
        async for job in page if page is not None else queryset:
            jobs.append(job.dataclass)

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
        return Response(DictEncoder().encode(Jobs(jobs=jobs, links=links)))

    async def aretrieve(self, request: GeoramaDrfRequest, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            return await super().aretrieve(request, *args, **kwargs)

        job = await self.aget_object()
        return Response(DictEncoder().encode(job.dataclass))

    @action(detail=True, methods=["post"], url_name="results")
    async def results(self, request: GeoramaDrfRequest, *args, **kwargs):
        _job = await self.aget_object()
        # result = _job.result()
        return Response("OK", status=status.HTTP_201_CREATED)
