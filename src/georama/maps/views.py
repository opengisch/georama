import logging

from asgiref.sync import sync_to_async
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View
from qgis_server_light.interface.dispatcher import RedisQueue
from qgis_server_light.interface.job import (
    QslGetFeatureInfoJob,
    WmsGetFeatureInfoParams,
    WmsGetMapParams,
)
from qgis_server_light.interface.qgis import Custom, Raster, Vector

from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.maps.apps import MapsConfig
from georama.maps.maps_config import Config
from georama.maps.models import PublishedAsWms
from georama.maps.services.wfs_2_0_0.get_capabilities import WfsGetCapabilities
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
            appname, f'{request.build_absolute_uri("maps")}?', request.user, self.model
        )
        if requested_format not in operation.allowed_formats:
            return HttpResponse(
                operation.render_operation_parsing_failed(
                    f"Format {requested_format} is not allowed. Allowed is {operation.allowed_formats}"
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
            appname, f'{request.build_absolute_uri("maps")}?', request.user, self.model
        )

        if requested_format not in operation.allowed_formats:
            return HttpResponse(
                operation.render_operation_parsing_failed(
                    f"Format {requested_format} is not allowed. Allowed is {operation.allowed_formats}"
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
            appname, f'{request.build_absolute_uri("maps")}?', request.user
        )
        if requested_layer:
            if requested_format not in operation.allowed_formats:
                return HttpResponse(
                    operation.render_operation_parsing_failed(
                        f"Format {requested_format} is not allowed. Allowed is {operation.allowed_formats}"
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
                    f"Query paramater 'layer' has to be set!"
                ),
                status=400,
                content_type="text/xml",
            )

    def sanitize_query_parameters(self, parameters: dict) -> dict:
        params = {}
        for key in parameters:
            if key.upper() == "LAYERS":
                params[str(key).upper()] = str(parameters[key])
            elif key.upper() == "STYLES":
                params[str(key).upper()] = str(parameters[key])
            elif key.upper() == "LAYER":
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
                    # since we will use this in the on a plain list of layers, the largest extent buffer
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

    async def get(self, request: HttpRequest, *args, **kwargs):
        # we instantiate vor every call because this is async and need to be in context of the calling event
        # loop
        redis_queue = await RedisQueue.create(Config().redis_url)

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
                service_params = WmsGetMapParams.from_overloaded_dict(params)
                operation = WmsGetMap(
                    appname, f'{request.build_absolute_uri("maps")}?', request.user, self.model
                )
                try:
                    job = await sync_to_async(
                        operation.prepare_job_content, thread_sensitive=True
                    )(service_params)
                except ValueError as e:
                    return HttpResponse(e, status=400, content_type="text/plain")
                except PermissionError as e:
                    return HttpResponse(e, status=403, content_type="text/plain")

            elif params["REQUEST"] == "GETFEATUREINFO":
                # this needs to be improved a bit, currently the layers are not sent to QSL.
                service_params = WmsGetFeatureInfoParams.from_overloaded_dict(params)
                job = QslGetFeatureInfoJob(service_params=service_params)
            else:
                return HttpResponse("Only WMS Service is available", 500)
            config = Config()
            try:
                result = await redis_queue.post(job, config.job_timeout)
                return HttpResponse(result.data, result.content_type)
            except RuntimeError:
                return HttpResponse(
                    "Something went wrong while job handling, see QSL logs for details",
                    status=500,
                    content_type="text/plain",
                )
        elif params["SERVICE"].upper() == "WFS":
            if params["REQUEST"] == "GETCAPABILITIES":
                if params.get("VERSION", "2.0.0") == "2.0.0":
                    return await sync_to_async(
                        self.wfs_200_capabilities, thread_sensitive=True
                    )(request, params)
                else:
                    return HttpResponse("Only VERSION 2.0.0 is available", 400)
        else:
            return HttpResponse("Only WMS|WFS Service is available", 400)


def admin_publish_dataset_as_wms(request: HttpRequest, dataset_type: str, dataset_id: str):
    """
    helper function to hide actual connection in the database but make publishing straight forward.
    """
    allowed_dataset_types = ["raster", "vector", "custom"]
    if dataset_type not in allowed_dataset_types:
        raise Http404
    if dataset_type == "raster":
        published_as_wms = PublishedAsWms(
            raster_dataset=RasterDataSet.objects.filter(id=dataset_id)[0]
        )
    elif dataset_type == "vector":
        published_as_wms = PublishedAsWms(
            vector_dataset=VectorDataSet.objects.filter(id=dataset_id)[0]
        )
    elif dataset_type == "custom":
        published_as_wms = PublishedAsWms(
            custom_dataset=CustomDataSet.objects.filter(id=dataset_id)[0]
        )
    else:
        raise Http404
    published_as_wms.save()
    return redirect("admin:maps_publishedaswms_changelist")
