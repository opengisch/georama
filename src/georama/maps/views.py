import logging
import os

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


def wms_130_capabilities(request: HttpRequest, params: dict) -> HttpResponse:
    url = request.build_absolute_uri()
    config = Config()
    parser = JsonParser()
    service = parser.from_string(config.service_config(url), Service)
    capapility = parser.from_string(config.capability_config(url), Capability)
    for published_as in PublishedAsWms.objects.all():
        if published_as.has_read_permission(request.user, appname):
            if isinstance(published_as.raster_dataset, RasterDataSet):
                dataset = published_as.raster_dataset
            elif isinstance(published_as.vector_dataset, VectorDataSet):
                dataset = published_as.vector_dataset
            elif isinstance(published_as.custom_dataset, CustomDataSet):
                dataset = published_as.custom_dataset
            else:
                raise NotImplementedError(
                    "linked dataset has to be RasterDataSet|VectorDataSet!"
                )
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
                if bbox_object not in capapility.layer.bounding_box:
                    capapility.layer.bounding_box.append(bbox_object)
            if bbox_4326 is not None:
                layer.bounding_box.append(bbox_4326)
                if bbox_4326 not in capapility.layer.bounding_box:
                    capapility.layer.bounding_box.append(bbox_4326)
            capapility.layer.layer.append(layer)
            capapility.layer.ex_geographic_bounding_box = ex_geographic_bounding_box_object

    wms_capabilities = WmsCapabilities(service=service, capability=capapility)

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
    request: HttpRequest, service_params: WmsGetMapParams
) -> tuple[list[Raster], list[Vector], list[Custom], float]:
    accessible_raster: list[Raster] = []
    accessible_vector: list[Vector] = []
    accessible_custom: list[Custom] = []
    # we set the extent buffer to zero, this is used to control rendering issues like
    # https://github.com/qgis/QGIS/issues/30251
    vector_extent_buffer = 0.0
    for published_as in PublishedAsWms.objects.filter(
        name__in=[name.lower() for name in service_params.layers]
    ):
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


async def entry(request: HttpRequest):
    # TODO: This is done because otherwise the queue cant be pointed to
    #   see this for further details: https://stackoverflow.com/questions/53724665/using-queues-results-in-asyncio-exception-got-future-future-pending-attached
    redis_queue = RedisQueue(Config().redis_url)
    params = {}
    for key in request.GET.dict():
        params[str(key).upper()] = str(request.GET[key]).upper()
    if "SERVICE" not in params:
        return HttpResponse("SERVICE parameter is mandatory", 500)
    if "REQUEST" not in params:
        return HttpResponse("REQUEST parameter is mandatory", 500)

    if params["SERVICE"] == "WMS":
        if params["REQUEST"] == "GETCAPABILITIES":
            if params.get("VERSION", "1.3.0") == "1.3.0":
                return await sync_to_async(wms_130_capabilities, thread_sensitive=True)(
                    request, params
                )
            else:
                return HttpResponse("Only VERSION 1.3.0 is available", 500)
        elif params["REQUEST"] == "GETMAP":
            service_params = WmsGetMapParams.from_overloaded_dict(params)
            (
                accessible_raster,
                accessible_vector,
                accessible_custom,
                vector_extent_buffer,
            ) = await sync_to_async(extract_layers, thread_sensitive=True)(
                request, service_params
            )

            job = QslGetMapJob(
                extent_buffer=vector_extent_buffer,
                service_params=service_params,
                raster_layers=accessible_raster,
                vector_layers=accessible_vector,
                custom_layers=accessible_custom,
            )
        elif params["REQUEST"] == "GETFEATUREINFO":
            # this needs to be improved a bit, currently the layers are not sent to QSL.
            service_params = WmsGetFeatureInfoParams.from_overloaded_dict(params)
            job = QslGetFeatureInfoJob(service_params=service_params)
        else:
            return HttpResponse("Only WMS Service is available", 500)
        result = await redis_queue.post(job, float(os.environ.get("JOB_TIMEOUT", 1000)))
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
