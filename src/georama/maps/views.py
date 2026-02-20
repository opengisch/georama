import logging

from asgiref.sync import sync_to_async
from django.apps import apps
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group, Permission, User
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import gettext as _
from django.views import View
from qgis_server_light.interface.dispatcher import RedisQueue
from qgis_server_light.interface.job import (
    JobResult,
    QslGetFeatureInfoJob,
    WmsGetFeatureInfoParams,
    WmsGetMapParams,
)
from qgis_server_light.interface.qgis import Custom, Raster, Vector
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import DictDecoder, XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import JsonSerializer

from georama.core.menu import BreadCrumb
from georama.core.services.permission import DBService
from georama.core.views.generic.delete import GeoramaDeleteView
from georama.core.views.generic.detail import GeoramaDetailView
from georama.core.views.generic.list import GeoramaListView
from georama.core.views.generic.mixins import (
    GeoramaAnyPermissionRequiredMixin,
    GeoramaLoginRequiredMixin,
)
from georama.core.views.generic.update import GeoramaUpdateView
from georama.core.views.multi_model.list import ChangeListView
from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.maps.apps import MapsConfig, central_app_label
from georama.maps.interfaces.georama.requests import QslGetMapRequest
from georama.maps.interfaces.ogc.wfs_2_0_0 import GetFeature as GetFeature200
from georama.maps.maps_config import Config
from georama.maps.models import PublishedAsWms
from georama.maps.services.services import DatasetService
from georama.maps.services.wfs_2_0_0.describe_feature_type import WfsDescribeFeatureType
from georama.maps.services.wfs_2_0_0.get_capabilities import WfsGetCapabilities
from georama.maps.services.wfs_2_0_0.get_feature import WfsGetFeature
from georama.maps.services.wfs_2_0_0.get_metadata import WfsGetMetadata
from georama.maps.services.wms_1_3_0.get_capabilities import WmsGetCapabilities
from georama.maps.services.wms_1_3_0.get_map import WmsGetMap

log = logging.getLogger(__name__)

appname = MapsConfig.get_simple_appname()


class OgcServer(View):
    model = PublishedAsWms

    def wms_130_capabilities(self, request: HttpRequest, params: dict) -> HttpResponse:
        """
        Handling the wms 1.3.0 capabilities.

        Args:
            request: The django request object.
            params: the parameters which were send.

        Returns:
            The response object.
        """
        requested_format = params.get("FORMAT", "TEXT/XML")
        operation = WmsGetCapabilities(
            appname, f'{request.build_absolute_uri("ows")}?', request.user, self.model
        )
        if requested_format not in operation.allowed_formats:
            return HttpResponse(
                operation.render_operation_parsing_failed(
                    f"Format {requested_format} is not allowed."
                    f"Allowed is {operation.allowed_formats}"
                ),
                status=400,
                content_type="text/xml",
            )
        if requested_format == "TEXT/XML":
            return HttpResponse(
                operation.render_xml(operation.get_capabilities()),
                content_type="text/xml",
            )
        elif requested_format == "APPLICATION/JSON":
            return HttpResponse(
                operation.render_json(operation.get_capabilities()),
                content_type="application/json",
            )

    def wfs_200_capabilities(self, request: HttpRequest, params: dict) -> HttpResponse:
        requested_format = params.get("FORMAT", "TEXT/XML")
        operation = WfsGetCapabilities(
            appname, f'{request.build_absolute_uri("ows")}?', request.user, self.model
        )

        if requested_format not in operation.allowed_formats:
            return HttpResponse(
                operation.render_operation_parsing_failed(
                    f"Format {requested_format} is not allowed."
                    f"Allowed is {operation.allowed_formats}"
                ),
                status=400,
                content_type="text/xml",
            )
        if requested_format == "TEXT/XML":
            return HttpResponse(
                operation.render_xml(operation.get_capabilities()),
                content_type="text/xml",
            )
        elif requested_format == "APPLICATION/JSON":
            return HttpResponse(
                operation.render_json(operation.get_capabilities()),
                content_type="application/json",
            )

    def wfs_get_metadata(self, request: HttpRequest, params: dict) -> HttpResponse:
        requested_layer = params.get("LAYER")
        language = "en-US"
        requested_format = params.get("FORMAT", "TEXT/XML")
        operation = WfsGetMetadata(
            appname, f'{request.build_absolute_uri("ows")}?', request.user, self.model
        )
        if requested_layer:
            if requested_format not in operation.allowed_formats:
                return HttpResponse(
                    operation.render_operation_parsing_failed(
                        f"Format {requested_format} is not allowed."
                        f"Allowed is {operation.allowed_formats}"
                    ),
                    status=400,
                    content_type="text/xml",
                )
            if requested_format == "TEXT/XML":
                return HttpResponse(
                    operation.render_xml(operation.get_metadata(requested_layer, language)),
                    content_type="text/xml",
                )
            elif requested_format == "APPLICATION/JSON":
                return HttpResponse(
                    operation.render_json(operation.get_metadata(requested_layer, language)),
                    content_type="application/json",
                )
        else:
            return HttpResponse(
                operation.render_operation_parsing_failed(
                    "Query paramater 'layer' has to be set!"
                ),
                status=400,
                content_type="text/xml",
            )

    def wfs_200_describefeaturetype(self, request: HttpRequest, params: dict) -> HttpResponse:
        # refering spec document `TYPENAME` is a comma separated
        # list of *layers* which should be described
        # it is an optional query parameter
        requested_layer = params.get("TYPENAME")
        if requested_layer:
            requested_layer = requested_layer.split(",")
        requested_format = params.get(
            "OUTPUTFORMAT", "APPLICATION/GML+XML; VERSION=3.2"
        ).upper()
        operation = WfsDescribeFeatureType(
            appname, f'{request.build_absolute_uri("ows")}?', request.user, self.model
        )
        content, content_type, success = operation.render(
            requested_format, operation.describe_feature_type(requested_layer)
        )
        if not success:
            return HttpResponse(
                content,
                status=400,
                content_type=content_type,
            )
        else:
            return HttpResponse(
                content,
                content_type=content_type,
            )

    async def wfs_200_getfeature(self, request: HttpRequest, params: dict) -> HttpResponse:
        operation = WfsGetFeature(
            appname, f'{request.build_absolute_uri("ows")}?', request.user, self.model
        )
        get_feature_parameter = operation.query_parameters_to_get_feature_request(params)

        job = await sync_to_async(
            operation.getfeature_to_qslgetfeaturejob, thread_sensitive=True
        )(get_feature_parameter)
        redis_queue = await self.redis_queue_instance
        result = await redis_queue.post(job, Config().job_timeout)
        content, content_type, success = operation.render(
            get_feature_parameter.output_format,
            operation.get_feature(
                # we use only one query here, since this is implemented
                # for URL GET query params
                # TODO: This has to be improved for XML body via POST
                get_feature_parameter,
                result,
                job,
            ),
            operation.unwrap_type_names(get_feature_parameter),
        )
        if not success:
            return HttpResponse(
                content,
                status=400,
                content_type=content_type,
            )
        else:
            return HttpResponse(
                content,
                content_type=content_type,
            )

    def sanitize_query_parameters(self, parameters: dict) -> dict:
        params = {}
        for key in parameters:
            if (
                key.upper() == "LAYERS"
                or key.upper() == "STYLES"
                or key.upper() == "TYPENAME"
                or key.upper() == "TYPENAMES"
                or key.upper() == "ALIASES"
                or key.upper() == "FILTER"
                or key.upper() == "LAYER"
            ):
                params[str(key).upper()] = str(parameters[key])
            else:
                params[str(key).upper()] = str(parameters[key]).upper()
        return params

    def extract_layers(
        self, request: HttpRequest, service_params: WmsGetMapParams
    ) -> tuple[list[Raster], list[Vector], list[Custom], float]:
        accessible_raster: list[Raster] = []
        accessible_vector: list[Vector] = []
        accessible_custom: list[Custom] = []
        # we set the extent buffer to zero, this is used to control rendering issues like
        # https://github.com/qgis/QGIS/issues/30251
        vector_extent_buffer = 0.0
        for published_as in self.model.objects.filter(name__in=service_params.layers):
            if published_as.has_read_permission(request.user, appname):
                if isinstance(published_as.raster_dataset, RasterDataSet):
                    accessible_raster.append(published_as.raster_dataset.to_qsl)
                elif isinstance(published_as.vector_dataset, VectorDataSet):
                    # since we will use this in the on a plain
                    # list of layers, the largest extent buffer
                    # should be applied
                    if published_as.extent_buffer > vector_extent_buffer:
                        vector_extent_buffer = published_as.extent_buffer
                    accessible_vector.append(published_as.vector_dataset.to_qsl)
                elif isinstance(published_as.custom_dataset, CustomDataSet):
                    accessible_custom.append(published_as.custom_dataset.to_qsl)
                else:
                    raise NotImplementedError(
                        "linked dataset has to be RasterDataSet|VectorDataSet!"
                    )
        return accessible_raster, accessible_vector, accessible_custom, vector_extent_buffer

    @property
    async def redis_queue_instance(self) -> RedisQueue:
        return await RedisQueue.create(Config().redis_url)

    async def get(self, request: HttpRequest, *args, **kwargs):
        params = self.sanitize_query_parameters(request.GET.dict())

        if "REQUEST" not in params:
            return HttpResponse("REQUEST parameter is mandatory", 400)

        if "SERVICE" not in params:
            if params["REQUEST"].upper() == "GETMETADATA":
                return await sync_to_async(self.wfs_get_metadata, thread_sensitive=True)(
                    request, params
                )
            else:
                return HttpResponse(
                    "Only request allowed without service param is GetMetadata", 400
                )

        if params["SERVICE"].upper() == "WMS":
            if params["REQUEST"] == "GETCAPABILITIES":
                if params.get("VERSION", "1.3.0") == "1.3.0":
                    return await sync_to_async(
                        self.wms_130_capabilities, thread_sensitive=True
                    )(request, params)
                else:
                    return HttpResponse("Only VERSION 1.3.0 is available", 400)
            elif params["REQUEST"] == "GETMAP":
                # This is especially usefull for input from foreign
                # systems which might send whatever query
                # params we don't have knowledge of
                parser_config = ParserConfig(
                    fail_on_unknown_properties=False, fail_on_unknown_attributes=False
                )
                service_params = DictDecoder(parser_config).decode(params, QslGetMapRequest)
                operation = WmsGetMap(
                    appname, f'{request.build_absolute_uri("ows")}?', request.user, self.model
                )
                try:
                    job = await sync_to_async(
                        operation.prepare_job_content, thread_sensitive=True
                    )(service_params)
                    logging.debug(JsonSerializer().render(job))
                except ValueError as e:
                    return HttpResponse(e, status=400, content_type="text/plain")
                except PermissionError as e:
                    return HttpResponse(e, status=403, content_type="text/plain")

            elif params["REQUEST"] == "GETFEATUREINFO":
                # TODO: this needs to be improved a bit, currently
                #  the layers are not sent to QSL.
                service_params = WmsGetFeatureInfoParams.from_overloaded_dict(params)
                job = QslGetFeatureInfoJob(service_params=service_params)
            else:
                return HttpResponse("Only WMS Service is available", 500)
            config = Config()
            try:
                redis_queue = await self.redis_queue_instance
                result = await redis_queue.post(job, config.job_timeout)
                return HttpResponse(result.data, result.content_type)
            except RuntimeError:
                return HttpResponse(
                    "Something went wrong while job handling, see QSL logs for details",
                    status=500,
                    content_type="text/plain",
                )
        elif params["SERVICE"].upper() == "WFS":
            if params.get("VERSION", "2.0.0") == "2.0.0":
                pass
            else:
                return HttpResponse("Only VERSION 2.0.0 is available", 400)
            if params["REQUEST"] == "GETCAPABILITIES":
                return await sync_to_async(self.wfs_200_capabilities, thread_sensitive=True)(
                    request, params
                )
            elif params["REQUEST"] == "DESCRIBEFEATURETYPE":
                return await sync_to_async(
                    self.wfs_200_describefeaturetype, thread_sensitive=True
                )(request, params)
            elif params["REQUEST"] == "GETFEATURE":
                try:
                    return await self.wfs_200_getfeature(request, params)
                except AttributeError as e:
                    return HttpResponse(e, status=400, content_type="text/xml")
                except PermissionError as e:
                    return HttpResponse(e, status=400, content_type="text/xml")
                # except Exception as e:
                #     logging.error(e)
                #     # TODO: Provide the error info also in the response if we are in DEBUG?
                #     return HttpResponse(
                #         "An unexpected error happened while processing the request",
                #         400
                #     )
            else:
                return HttpResponse("Not supported operation", 403)
        else:
            return HttpResponse("Only WMS|WFS Service is available", 400)

    async def post(self, request: HttpRequest, *args, **kwargs):
        try:
            operation = WfsGetFeature(
                appname, f'{request.build_absolute_uri("ows")}?', request.user, self.model
            )
            try:
                get_feature_parameter = XmlParser().from_bytes(request.body, GetFeature200)
                job = await sync_to_async(
                    operation.getfeature_to_qslgetfeaturejob, thread_sensitive=True
                )(get_feature_parameter)
            except ParserError as e:
                logging.error(e)
                return HttpResponse(
                    WfsGetFeature.render_exception("Could not parse payload"),
                    status=400,
                    content_type="text/xml",
                )
            redis_queue = await self.redis_queue_instance
            result: JobResult = await redis_queue.post(job, Config().job_timeout)
            content, content_type, success = operation.render(
                get_feature_parameter.output_format.upper(),
                operation.get_feature(
                    # we use only one query here, since this is
                    # implemented for URL GET query params
                    # TODO: This has to be improved for XML body via POST
                    get_feature_parameter,
                    result,
                    job,
                ),
                operation.unwrap_type_names(get_feature_parameter),
            )
            if not success:
                return HttpResponse(
                    content,
                    status=400,
                    content_type=content_type,
                )
            else:
                return HttpResponse(
                    content,
                    content_type=content_type,
                )
        except AttributeError as e:
            logging.error(e)
            return HttpResponse(e, status=400, content_type="text/xml")


class PublishLayer(GeoramaLoginRequiredMixin, PermissionRequiredMixin, View):
    model = PublishedAsWms
    permission_required = model.perm_add()

    def get(self, request: HttpRequest, dataset_type: str, dataset_id: str):
        """
        helper function to hide actual connection in the database but make
        publishing straight forward.
        """
        allowed_dataset_types = ["raster", "vector", "custom"]
        if dataset_type not in allowed_dataset_types:
            raise Http404
        if dataset_type == "raster":
            published_as_wms = self.model(
                raster_dataset=RasterDataSet.objects.filter(id=dataset_id)[0]
            )
        elif dataset_type == "vector":
            published_as_wms = self.model(
                vector_dataset=VectorDataSet.objects.filter(id=dataset_id)[0]
            )
        elif dataset_type == "custom":
            published_as_wms = self.model(
                custom_dataset=CustomDataSet.objects.filter(id=dataset_id)[0]
            )
        else:
            raise Http404
        published_as_wms.save()

        next_url = request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
        ):
            return redirect(next_url)
        return redirect(f"{central_app_label}:layer-list")


class Index(GeoramaListView):
    """
    This view is the apps landing page. It shows the available published
    layers a user can access. This is also available in public and shows
    layers which are public too. However, the important part is, that we
    use the Georama inherent ObjectPermissionSystem `PublishedAs` here.
    Not the Django model permission system.
    """

    model = PublishedAsWms
    template_name = "maps/index.html"

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title),
        ]

    def get_queryset(self):
        permitted_layers = []
        layers = self.model.objects.all()
        for layer in layers:
            if layer.has_general_permission(self.request.user, central_app_label):
                permitted_layers.append(layer)
        return permitted_layers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (
            self.request.user.has_perm(self.model.perm_view())
            or self.request.user.has_perm(self.model.perm_change())
            or self.request.user.has_perm(self.model.perm_delete())
            or self.request.user.has_perm(self.model.perm_add())
            or self.request.user.has_perm(self.model.perm_manage_permissions())
        ):
            context["breadcrumb_action_url"] = f"{central_app_label}:layer-list"
            context["breadcrumb_action_icon"] = "fa fa-wrench"
            context["breadcrumb_action_title"] = _("Manage Layers")
            context["breadcrumb_action_tooltip"] = _("Manage published layers")
        context["wms_get_capabilities_params"] = (
            self.model.create_wms_capabilities_url_params()
        )
        context["wfs_get_capabilities_params"] = (
            self.model.create_wfs_capabilities_url_params()
        )
        return context


class LayerListView(
    GeoramaLoginRequiredMixin, GeoramaAnyPermissionRequiredMixin, GeoramaListView
):
    model = PublishedAsWms
    template_name = "maps/list.html"
    permission_required = [
        model.perm_view(),
        model.perm_change(),
        model.perm_delete(),
        model.perm_add(),
        model.perm_manage_permissions(),
    ]

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers")),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.has_perm(self.model.perm_add()):
            context["breadcrumb_action_url"] = f"{central_app_label}:layer-source-list"
            context["breadcrumb_action_icon"] = "fa fa-circle-plus"
            context["breadcrumb_action_title"] = _("publish layer")
            context["breadcrumb_action_tooltip"] = _("Publish a new maps layer")
        return context


class PublishListView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, ChangeListView):
    """
    We use a special type of view here since it need to deal with subclassed models
    which should be listed in one list for selection.
    """

    service = DatasetService
    title = "Publish"
    name = "layer-source-list"
    app_menu = apps.get_app_config("maps").app_menu()
    template = "maps/publish.html"
    breadcrumbs = [
        BreadCrumb(app_menu.title, f"{app_menu.app_label}:index"),
        BreadCrumb(_("Manage Layers"), reverse_lazy(f"{app_menu.app_label}:layer-list")),
        BreadCrumb(_("Add")),
    ]
    permission_required = PublishedAsWms.perm_add()


class MapDetailView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaDetailView):
    model = PublishedAsWms
    template_name = "maps/detail.html"
    permission_required = model.perm_view()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(self.object.title or self.object.name),
        ]

    def get_context_data(self, **kwargs):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        context = super().get_context_data(**kwargs)
        context["update_view_name"] = f"{app_menu.app_label}:layer-update"
        context["delete_view_name"] = f"{app_menu.app_label}:layer-delete"
        context["permission_view_name"] = f"{app_menu.app_label}:layer-permission-list"
        context["perm_change"] = self.request.user.has_perm(self.model.perm_change())
        context["perm_manage_permission"] = self.request.user.has_perm(
            self.model.perm_manage_permissions()
        )
        context["perm_delete"] = self.request.user.has_perm(self.model.perm_delete())
        return context


class MapUpdateView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaUpdateView):
    model = PublishedAsWms
    fields = [
        "title",
        "name",
        "description",
        "public",
        "queryable",
        "license",
        "fees",
        "access_constraints",
    ]
    permission_required = model.perm_change()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(
                self.object.title or self.object.name,
                reverse(
                    f"{app_menu.app_label}:layer-detail", kwargs={"pk": self.kwargs["pk"]}
                ),
            ),
        ]

    def get_context_data(self, **kwargs):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        context = super().get_context_data(**kwargs)
        context["delete_view_name"] = f"{app_menu.app_label}:layer-delete"
        context["permission_view_name"] = f"{app_menu.app_label}:layer-permission-list"
        context["perm_manage_permission"] = self.request.user.has_perm(
            self.model.perm_manage_permissions()
        )
        context["perm_delete"] = self.request.user.has_perm(self.model.perm_delete())
        return context


class MapDeleteView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaDeleteView):
    model = PublishedAsWms
    success_url = reverse_lazy(f"{central_app_label}:layer-list")
    permission_required = model.perm_delete()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(
                self.object.title or self.object.name,
                reverse(
                    f"{app_menu.app_label}:layer-detail", kwargs={"pk": self.kwargs["pk"]}
                ),
            ),
        ]


class PermissionView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaDetailView):
    model = Permission
    template_name = "core/permission.html"
    permission_required = PublishedAsWms.perm_manage_permissions()

    def get_object(self, queryset=None):
        object_pk = self.kwargs.get("pk")
        dbs_permission = DBService(PublishedAsWms, central_app_label)
        return dbs_permission.get_permission_lookup(object_pk)

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(
                PublishedAsWms.objects.get(pk=self.kwargs.get("pk")).title,
                reverse(
                    f"{app_menu.app_label}:layer-detail", kwargs={"pk": self.kwargs.get("pk")}
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_user_url"] = reverse(
            f"{central_app_label}:layer-permission-user-list",
            kwargs={"pk": self.kwargs.get("pk")},
        )
        context["add_group_url"] = reverse(
            f"{central_app_label}:layer-permission-group-list",
            kwargs={"pk": self.kwargs.get("pk")},
        )
        return context


class UserListView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaListView):
    model = User
    template_name = "core/user.html"
    permission_required = PublishedAsWms.perm_manage_permissions()

    def get_queryset(self):
        return (
            User.objects.exclude(
                user_permissions__codename__icontains=str(self.kwargs.get("pk"))
            )
            .exclude(pk=None)
            .filter(is_superuser=False)
        )

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(
                PublishedAsWms.objects.get(pk=self.kwargs.get("pk")).title,
                reverse(
                    f"{app_menu.app_label}:layer-detail", kwargs={"pk": self.kwargs.get("pk")}
                ),
            ),
            BreadCrumb(
                PermissionView.model._meta.verbose_name,
                reverse(
                    f"{app_menu.app_label}:layer-permission-list",
                    kwargs={"pk": self.kwargs.get("pk")},
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dbs_permission = DBService(PublishedAsWms, central_app_label)
        context["read_permission_id"] = (
            dbs_permission.get_by_object_pk(self.kwargs.get("pk"))
            .filter(codename__icontains="read")
            .get()
            .pk
        )
        context["success_url"] = reverse(
            "maps:layer-permission-list", kwargs={"pk": self.kwargs.get("pk")}
        )
        return context


class GroupListView(GeoramaListView):
    model = Group
    template_name = "core/group.html"

    def get_queryset(self):
        return Group.objects.exclude(
            permissions__codename__icontains=str(self.kwargs.get("pk"))
        )

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:layer-list")),
            BreadCrumb(
                PublishedAsWms.objects.get(pk=self.kwargs.get("pk")).title,
                reverse(
                    f"{app_menu.app_label}:layer-detail", kwargs={"pk": self.kwargs.get("pk")}
                ),
            ),
            BreadCrumb(
                PermissionView.model._meta.verbose_name,
                reverse(
                    f"{app_menu.app_label}:layer-permission-list",
                    kwargs={"pk": self.kwargs.get("pk")},
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dbs_permission = DBService(PublishedAsWms, central_app_label)
        context["read_permission_id"] = (
            dbs_permission.get_by_object_pk(self.kwargs.get("pk"))
            .filter(codename__icontains="read")
            .get()
            .pk
        )
        context["success_url"] = reverse(
            "maps:layer-permission-list", kwargs={"pk": self.kwargs.get("pk")}
        )
        return context
