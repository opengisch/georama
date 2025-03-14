import logging
import time
from typing import List, Tuple

from asgiref.sync import sync_to_async
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from qgis_server_light.interface.dispatcher import RedisQueue
from qgis_server_light.interface.job import (
    QslGetFeatureInfoJob,
    QslGetMapJob,
    WmsGetFeatureInfoParams,
    WmsGetMapParams,
)
from qgis_server_light.interface.qgis import BBox
from qgis_server_light.interface.qgis import Crs as QSL_Crs
from qgis_server_light.interface.qgis import Custom, Raster, Vector
from xsdata.formats.dataclass.parsers import DictDecoder, JsonParser
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer

from georama.data_integration.models import CustomDataSet, RasterDataSet, VectorDataSet
from georama.maps.apps import appname
from georama.maps.interfaces.ogc.wms_1_3_0.capabilities.capabilities_1_3_0 import (
    BoundingBox,
    Capability,
    Crs,
    ExGeographicBoundingBox,
    Layer,
    Name,
    Service,
    Style,
    Title,
    WmsCapabilities,
)
from georama.maps.maps_config import Config
from georama.maps.models import PublishedAsWms

log = logging.getLogger(__name__)


def wms_130_capabilities(
    request: HttpRequest, params: dict, mandant: str | None = None, project: str | None = None
) -> HttpResponse:
    url = request.build_absolute_uri()
    config = Config()
    parser = JsonParser()
    service = parser.from_string(config.service_config(url), Service)
    capability = parser.from_string(config.capability_config(url), Capability)

    for published_as in PublishedAsWms.objects.all():
        if published_as.has_read_permission(request.user, appname):
            dataset = published_as.bound_dataset
            if project and mandant:
                if dataset.project.mandant.name != mandant:
                    continue
                if dataset.project.name != project:
                    continue
            elif mandant and not project:
                if dataset.project.mandant.name != mandant:
                    continue
            source_crs = DictDecoder().decode(dataset.crs, QSL_Crs)

            bbox_object = None
            try:
                bbox = BBox.from_string(dataset.bbox)
                bbox_object = BoundingBox(
                    crs=source_crs.auth_id,
                    minx=bbox.x_min,
                    maxx=bbox.x_max,
                    miny=bbox.y_min,
                    maxy=bbox.y_max,
                )
            except Exception:
                log.info(f'no BBOX could created from string: "{dataset.bbox}"')

            ex_geographic_bounding_box_object = None
            bbox_4326 = None
            try:
                bbox_wgs84 = BBox.from_string(dataset.bbox_wgs84)
                ex_geographic_bounding_box_object = ExGeographicBoundingBox(
                    west_bound_longitude=bbox_wgs84.x_min,
                    east_bound_longitude=bbox_wgs84.x_max,
                    south_bound_latitude=bbox_wgs84.y_min,
                    north_bound_latitude=bbox_wgs84.y_max,
                )
                bbox_4326 = BoundingBox(
                    crs="EPSG:4326",
                    minx=bbox_wgs84.x_min,
                    maxx=bbox_wgs84.x_max,
                    miny=bbox_wgs84.y_min,
                    maxy=bbox_wgs84.y_max,
                )
            except Exception:
                log.info(
                    f'no bbox_4326 and bbox_wgs84 could created from string: "{dataset.bbox_wgs84}"'
                )
            layer = Layer(
                queryable=False,
                cascaded=0,
                name=Name(published_as.name),
                title=published_as.title,
                abstract=published_as.description,
                crs=[Crs(source_crs.auth_id), Crs("CRS:84")],
                ex_geographic_bounding_box=ex_geographic_bounding_box_object,
                bounding_box=[bbox_object, bbox_4326],
                style=[Style(name=Name("default"), title=Title("Default"))],
            )
            if bbox_object is not None:
                layer.bounding_box.append(bbox_object)
                if bbox_object not in capability.layer.bounding_box:
                    capability.layer.bounding_box.append(bbox_object)
            if bbox_4326 is not None:
                layer.bounding_box.append(bbox_4326)
                if bbox_4326 not in capability.layer.bounding_box:
                    capability.layer.bounding_box.append(bbox_4326)
            capability.layer.layer.append(layer)
            capability.layer.ex_geographic_bounding_box = ex_geographic_bounding_box_object

    wms_capabilities = WmsCapabilities(service=service, capability=capability)

    allowed_formats = ["TEXT/XML", "APPLICATION/JSON"]
    requested_format = params.get("FORMAT", "TEXT/XML")
    if requested_format not in allowed_formats:
        requested_format = "TEXT/XML"
    print(requested_format)
    if requested_format == "TEXT/XML":
        serializer = XmlSerializer()
        return HttpResponse(
            serializer.render(
                wms_capabilities,
                ns_map={
                    None: "http://www.opengis.net/wms",
                    "xlink": "http://www.w3.org/1999/xlink",
                },
            ),
            content_type="text/xml",
        )
    elif requested_format == "APPLICATION/JSON":
        serializer = JsonSerializer()
        return HttpResponse(
            serializer.render(wms_capabilities), content_type="application/json"
        )


def extract_layers(
    user_permissions: List[str], user_is_super_user: bool, service_params: WmsGetMapParams
) -> tuple[list[Raster], list[Vector], list[Custom], float]:
    accessible_raster: list[Raster] = []
    accessible_vector: list[Vector] = []
    accessible_custom: list[Custom] = []
    # we set the extent buffer to zero, this is used to control rendering issues like
    # https://github.com/qgis/QGIS/issues/30251
    vector_extent_buffer = 0.0
    for published_as in PublishedAsWms.objects.filter(name__in=service_params.layers):
        if user_is_super_user or published_as.has_read_permission(user_permissions, appname):
            if isinstance(published_as.raster_dataset, RasterDataSet):
                accessible_raster.append(published_as.raster_dataset.to_qsl(published_as.name))
            elif isinstance(published_as.vector_dataset, VectorDataSet):
                # since we will use this in the on a plain list of layers, the largest extent buffer
                # should be applied
                if published_as.extent_buffer > vector_extent_buffer:
                    vector_extent_buffer = published_as.extent_buffer
                accessible_vector.append(published_as.vector_dataset.to_qsl(published_as.name))
            elif isinstance(published_as.custom_dataset, CustomDataSet):
                accessible_custom.append(published_as.custom_dataset.to_qsl(published_as.name))
            else:
                raise NotImplementedError(
                    "linked dataset has to be RasterDataSet|VectorDataSet!"
                )
    return accessible_raster, accessible_vector, accessible_custom, vector_extent_buffer


async def global_aggregated(request: HttpRequest):
    return await entry(request)


async def global_mandant_aggregated(request: HttpRequest, mandant: str):
    return await entry(request, mandant=mandant)


async def global_mandant_and_project_aggregated(
    request: HttpRequest, mandant: str, project: str
):
    return await entry(request, mandant=mandant, project=project)


def get_user_permissions(request: HttpRequest) -> Tuple[List[str], bool]:
    return request.user.get_all_permissions(), request.user.is_superuser


async def entry(request: HttpRequest, mandant: str | None = None, project: str | None = None):
    # TODO: This is done because otherwise the queue cant be pointed to
    #   see this for further details: https://stackoverflow.com/questions/53724665/using-queues-results-in-asyncio-exception-got-future-future-pending-attached
    redis_queue = RedisQueue(Config().redis_url)
    params = {}
    # we access user stuff once, instead of looping and accesing it all over again
    start_user_permission_collection = time.time()
    user_permissions, user_is_super_user = await sync_to_async(
        get_user_permissions, thread_sensitive=True
    )(request)
    end_user_permission_collection = time.time()
    log.error(
        f"Permission check took: {round(1000 * (end_user_permission_collection - start_user_permission_collection), 2)}ms"
    )
    for key in request.GET.dict():
        if key.upper() == "LAYERS":
            params[str(key).upper()] = str(request.GET[key])
        else:
            params[str(key).upper()] = str(request.GET[key]).upper()
    if "SERVICE" not in params:
        return HttpResponse("SERVICE parameter is mandatory", 500)
    if "REQUEST" not in params:
        return HttpResponse("REQUEST parameter is mandatory", 500)

    if params["SERVICE"].upper() == "WMS":
        if params["REQUEST"] == "GETCAPABILITIES":
            if params.get("VERSION", "1.3.0") == "1.3.0":
                return await sync_to_async(wms_130_capabilities, thread_sensitive=True)(
                    request, params, mandant, project
                )
            else:
                return HttpResponse("Only VERSION 1.3.0 is available", 500)
        elif params["REQUEST"] == "GETMAP":
            start_permission_check = time.time()
            service_params = WmsGetMapParams.from_overloaded_dict(params)
            (
                accessible_raster,
                accessible_vector,
                accessible_custom,
                vector_extent_buffer,
            ) = await sync_to_async(extract_layers, thread_sensitive=True)(
                user_permissions, user_is_super_user, service_params
            )
            job = QslGetMapJob(
                extent_buffer=vector_extent_buffer,
                service_params=service_params,
                raster_layers=accessible_raster,
                vector_layers=accessible_vector,
                custom_layers=accessible_custom,
            )
            end_permission_check = time.time()
            log.error(
                f"Permission check took: {round(1000 * (end_permission_check - start_permission_check), 2)}ms"
            )
        elif params["REQUEST"] == "GETFEATUREINFO":
            # this needs to be improved a bit, currently the layers are not sent to QSL.
            service_params = WmsGetFeatureInfoParams.from_overloaded_dict(params)
            job = QslGetFeatureInfoJob(service_params=service_params)
        else:
            return HttpResponse("Only WMS Service is available", 500)
        config = Config()
        start_rendering = time.time()
        result = await redis_queue.post(job, config.job_timeout)
        end_rendering = time.time()
        log.error(f"Rendering took: {round(1000 * (end_rendering - start_rendering), 2)}ms")
        return HttpResponse(result.data, result.content_type)
    else:
        return HttpResponse("Only WMS Service is available", 500)


def admin_publish_raster_as_wms(request: HttpRequest, dataset_id: str):
    """
    helper function to hide actual connection in the database but make publishing straight forward.
    """

    published_as_wms = PublishedAsWms(
        raster_dataset=RasterDataSet.objects.filter(id=dataset_id)[0]
    )
    published_as_wms.save()
    return redirect("admin:maps_publishedaswms_changelist")


def admin_publish_vector_as_wms(request: HttpRequest, dataset_id: str):
    """
    helper function to hide actual connection in the database but make publishing straight forward.
    """

    published_as_wms = PublishedAsWms(
        vector_dataset=VectorDataSet.objects.filter(id=dataset_id)[0]
    )
    published_as_wms.save()
    return redirect("admin:maps_publishedaswms_changelist")


def admin_publish_custom_as_wms(request: HttpRequest, dataset_id: str):
    """
    helper function to hide actual connection in the database but make publishing straight forward.
    """

    published_as_wms = PublishedAsWms(
        custom_dataset=CustomDataSet.objects.filter(id=dataset_id)[0]
    )
    published_as_wms.save()
    return redirect("admin:maps_publishedaswms_changelist")
