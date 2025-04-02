import logging
from xml.etree.ElementTree import QName

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
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.comparison_operator_type import (
    ComparisonOperatorType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.comparison_operators_type import (
    ComparisonOperatorsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.filter_capabilities import (
    ConformanceType,
    FilterCapabilities,
    IdCapabilitiesType,
    ScalarCapabilitiesType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.geometry_operands_type import (
    GeometryOperandsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.resource_identifier_type import (
    ResourceIdentifierType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.spatial_capabilities_type import (
    SpatialCapabilitiesType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.spatial_operator_type import (
    SpatialOperatorType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.spatial_operators_type import (
    SpatialOperatorsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.temporal_capabilities_type import (
    TemporalCapabilitiesType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.temporal_operands_type import (
    TemporalOperandsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.temporal_operator_name_type_value import (
    TemporalOperatorNameTypeValue,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.temporal_operator_type import (
    TemporalOperatorType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.temporal_operators_type import (
    TemporalOperatorsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1 import (
    DefaultValue,
    OnlineResourceType,
    RequestMethodType,
    Value,
    Wgs84BoundingBox,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.access_constraints import (
    AccessConstraints as WfsAccessConstraints,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.allowed_values import (
    AllowedValues,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.code_type import (
    CodeType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.dcp import Dcp
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.domain_type import (
    DomainType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.fees import Fees
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.http import Http
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.operation import (
    Operation,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.operations_metadata import (
    OperationsMetadata,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.service_identification import (
    ServiceIdentification,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.service_provider import (
    ServiceProvider,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.title import (
    Title as OwsTitle,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2 import (
    FeatureTypeType,
    OutputFormatListType,
    WfsCapabilitiesType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.feature_type_list import (
    FeatureTypeList,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.title import (
    Title as WfsTitle,
)
from georama.maps.interfaces.ogc.wms_1_3_0.capabilities.capabilities_1_3_0 import (
    BoundingBox,
    Capability,
    Crs,
    ExGeographicBoundingBox,
    Layer,
    Name,
)
from georama.maps.interfaces.ogc.wms_1_3_0.capabilities.capabilities_1_3_0 import (
    Service as ServiceWms,
)
from georama.maps.interfaces.ogc.wms_1_3_0.capabilities.capabilities_1_3_0 import (
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
    service = parser.from_string(config.service_config(url), ServiceWms)
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
                    "linked dataset has to be RasterDataSet|VectorDataSet|CustomDataSet!"
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


def wfs_200_capabilities(request: HttpRequest, params: dict) -> HttpResponse:
    url = f'{request.build_absolute_uri("maps")}?'
    service_identification = ServiceIdentification(
        title=[OwsTitle(value="Georama WFS")],
        service_type=CodeType(code_space="OGC", value="WFS"),
        service_type_version=["2.0.0"],
        fees=Fees("None"),
        access_constraints=[WfsAccessConstraints("None")],
    )
    service_provider = ServiceProvider(
        "OPENGIS.ch", OnlineResourceType(href="https://opengis.ch")
    )
    get_capability_operation = Operation(
        name="GetCapabilities",
        dcp=[Dcp(Http(get=[RequestMethodType(href=url)], post=[RequestMethodType(href=url)]))],
        parameter=[
            DomainType(name="AcceptVersions", allowed_values=AllowedValues([Value("2.0.0")])),
            DomainType(
                name="AcceptFormats", allowed_values=AllowedValues([Value("text/xml")])
            ),
            DomainType(
                name="Sections",
                allowed_values=AllowedValues(
                    [
                        Value("ServiceIdentification"),
                        Value("ServiceProvider"),
                        Value("OperationsMetadata"),
                        Value("FeatureTypeList"),
                        Value("Filter_Capabilities"),
                    ]
                ),
            ),
        ],
    )
    describe_feature_type_operation = Operation(
        name="DescribeFeatureType",
        dcp=[Dcp(Http(get=[RequestMethodType(href=url)], post=[RequestMethodType(href=url)]))],
        parameter=[
            DomainType(
                name="outputFormat",
                allowed_values=AllowedValues(
                    [
                        Value("application/gml+xml; version=3.2"),
                        Value("text/xml; subtype=gml/3.2.1"),
                        Value("text/xml; subtype=gml/3.1.1"),
                        Value("text/xml; subtype=gml/2.1.2"),
                    ]
                ),
            )
        ],
    )
    get_features_operation = Operation(
        name="GetFeature",
        dcp=[Dcp(Http(get=[RequestMethodType(href=url)], post=[RequestMethodType(href=url)]))],
        parameter=[
            DomainType(
                name="outputFormat",
                allowed_values=AllowedValues(
                    [
                        Value("application/gml+xml; version=3.2"),
                        Value("text/xml; subtype=gml/3.2.1"),
                        Value("text/xml; subtype=gml/3.1.1"),
                        Value("text/xml; subtype=gml/2.1.2"),
                    ]
                ),
            )
        ],
    )
    get_property_value_operation = Operation(
        name="GetPropertyValue",
        dcp=[Dcp(Http(get=[RequestMethodType(href=url)], post=[RequestMethodType(href=url)]))],
        parameter=[
            DomainType(
                name="outputFormat",
                allowed_values=AllowedValues(
                    [
                        Value("application/gml+xml; version=3.2"),
                        Value("text/xml; subtype=gml/3.2.1"),
                        Value("text/xml; subtype=gml/3.1.1"),
                        Value("text/xml; subtype=gml/2.1.2"),
                    ]
                ),
            )
        ],
    )
    get_list_stored_queries_operation = Operation(
        name="ListStoredQueries",
        dcp=[Dcp(Http(get=[RequestMethodType(href=url)], post=[RequestMethodType(href=url)]))],
    )
    get_describe_stored_queries_operation = Operation(
        name="DescribeStoredQueries",
        dcp=[Dcp(Http(get=[RequestMethodType(href=url)], post=[RequestMethodType(href=url)]))],
    )
    operations_metadata = OperationsMetadata(
        operation=[
            get_capability_operation,
            describe_feature_type_operation,
            get_features_operation,
            get_property_value_operation,
            # TODO: check if we need that really!
            get_list_stored_queries_operation,
            get_describe_stored_queries_operation,
        ],
        parameter=[DomainType(name="version", allowed_values=AllowedValues([Value("2.0.0")]))],
        constraint=[
            DomainType(name="ImplementsBasicWFS", default_value=DefaultValue("TRUE")),
            DomainType(name="ImplementsTransactionalWFS", default_value=DefaultValue("FALSE")),
            DomainType(name="ImplementsLockingWFS", default_value=DefaultValue("FALSE")),
            DomainType(name="KVPEncoding", default_value=DefaultValue("FALSE")),
            DomainType(name="XMLEncoding", default_value=DefaultValue("TRUE")),
            DomainType(name="SOAPEncoding", default_value=DefaultValue("FALSE")),
            DomainType(name="ImplementsInheritance", default_value=DefaultValue("FALSE")),
            DomainType(name="ImplementsRemoteResolve", default_value=DefaultValue("FALSE")),
            DomainType(name="ImplementsResultPaging", default_value=DefaultValue("TRUE")),
            DomainType(name="ImplementsStandardJoins", default_value=DefaultValue("FALSE")),
            DomainType(name="ImplementsSpatialJoins", default_value=DefaultValue("FALSE")),
            DomainType(name="ImplementsTemporalJoins", default_value=DefaultValue("FALSE")),
            DomainType(
                name="ImplementsFeatureVersioning", default_value=DefaultValue("FALSE")
            ),
            DomainType(name="ManageStoredQueries", default_value=DefaultValue("FALSE")),
            DomainType(name="PagingIsTransactionSafe", default_value=DefaultValue("FALSE")),
            DomainType(
                name="QueryExpressions",
                allowed_values=AllowedValues(
                    value=[Value("wfs:Query"), Value("wfs:StoredQuery")]
                ),
            ),
        ],
    )
    filter_capabilities = FilterCapabilities(
        conformance=ConformanceType(
            constraint=[
                DomainType(name="ImplementsQuery", default_value=DefaultValue("TRUE")),
                DomainType(name="ImplementsAdHocQuery", default_value=DefaultValue("TRUE")),
                DomainType(name="ImplementsFunctions", default_value=DefaultValue("FALSE")),
                DomainType(name="ImplementsResourceId", default_value=DefaultValue("TRUE")),
                DomainType(
                    name="ImplementsMinStandardFilter", default_value=DefaultValue("TRUE")
                ),
                DomainType(
                    name="ImplementsStandardFilter", default_value=DefaultValue("TRUE")
                ),
                DomainType(
                    name="ImplementsMinSpatialFilter", default_value=DefaultValue("TRUE")
                ),
                DomainType(
                    name="ImplementsSpatialFilter", default_value=DefaultValue("FALSE")
                ),
                DomainType(
                    name="ImplementsMinTemporalFilter", default_value=DefaultValue("TRUE")
                ),
                DomainType(
                    name="ImplementsTemporalFilter", default_value=DefaultValue("FALSE")
                ),
                DomainType(name="ImplementsVersionNav", default_value=DefaultValue("FALSE")),
                DomainType(name="ImplementsSorting", default_value=DefaultValue("TRUE")),
                DomainType(
                    name="ImplementsExtendedOperators", default_value=DefaultValue("FALSE")
                ),
                DomainType(name="ImplementsMinimumXPath", default_value=DefaultValue("TRUE")),
                DomainType(
                    name="ImplementsSchemaElementFunc", default_value=DefaultValue("FALSE")
                ),
            ]
        ),
        id_capabilities=IdCapabilitiesType(
            resource_identifier=[ResourceIdentifierType(name=QName("fes:ResourceId"))]
        ),
        scalar_capabilities=ScalarCapabilitiesType(
            comparison_operators=ComparisonOperatorsType(
                comparison_operator=[
                    ComparisonOperatorType(name="PropertyIsEqualTo"),
                    ComparisonOperatorType(name="PropertyIsNotEqualTo"),
                    ComparisonOperatorType(name="PropertyIsLessThan"),
                    ComparisonOperatorType(name="PropertyIsGreaterThan"),
                    ComparisonOperatorType(name="PropertyIsLessThanOrEqualTo"),
                    ComparisonOperatorType(name="PropertyIsGreaterThanOrEqualTo"),
                    ComparisonOperatorType(name="PropertyIsLike"),
                    ComparisonOperatorType(name="PropertyIsBetween"),
                ]
            )
        ),
        spatial_capabilities=SpatialCapabilitiesType(
            geometry_operands=GeometryOperandsType(
                geometry_operand=[
                    GeometryOperandsType.GeometryOperand(name=QName("gml:Point")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:MultiPoint")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:LineString")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:MultiLineString")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:Curve")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:MultiCurve")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:Polygon")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:MultiPolygon")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:Surface")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:MultiSurface")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:Box")),
                    GeometryOperandsType.GeometryOperand(name=QName("gml:Envelope")),
                ]
            ),
            spatial_operators=SpatialOperatorsType(
                spatial_operator=[
                    SpatialOperatorType(
                        geometry_operands=GeometryOperandsType(
                            geometry_operand=[
                                GeometryOperandsType.GeometryOperand(name=QName("Equals")),
                                GeometryOperandsType.GeometryOperand(name=QName("Disjoint")),
                                GeometryOperandsType.GeometryOperand(name=QName("Touches")),
                                GeometryOperandsType.GeometryOperand(name=QName("Within")),
                                GeometryOperandsType.GeometryOperand(name=QName("Overlaps")),
                                GeometryOperandsType.GeometryOperand(name=QName("Crosses")),
                                GeometryOperandsType.GeometryOperand(name=QName("Intersects")),
                                GeometryOperandsType.GeometryOperand(name=QName("Contains")),
                                GeometryOperandsType.GeometryOperand(name=QName("DWithin")),
                                GeometryOperandsType.GeometryOperand(name=QName("Beyond")),
                                GeometryOperandsType.GeometryOperand(name=QName("BBOX")),
                            ]
                        )
                    )
                ]
            ),
        ),
        temporal_capabilities=TemporalCapabilitiesType(
            temporal_operands=TemporalOperandsType(
                temporal_operand=[
                    TemporalOperandsType.TemporalOperand(name=QName("gml:TimePeriod")),
                    TemporalOperandsType.TemporalOperand(name=QName("gml:TimeInstant")),
                ]
            ),
            temporal_operators=TemporalOperatorsType(
                temporal_operator=[
                    TemporalOperatorType(name=TemporalOperatorNameTypeValue.DURING)
                ]
            ),
        ),
    )
    feature_type_list = FeatureTypeList()
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
                    "linked dataset has to be RasterDataSet|VectorDataSet|CustomDataSet!"
                )
            source_crs = DictDecoder().decode(dataset.crs, QSL_Crs)

            bbox_object = None
            try:
                bbox = BBox.from_string(dataset.bbox_wgs84)
                bbox_object = BoundingBox(
                    crs=source_crs.auth_id,
                    minx=bbox.x_min,
                    maxx=bbox.x_max,
                    miny=bbox.y_min,
                    maxy=bbox.y_max,
                )
            except Exception:
                log.info(f'no BBOX could created from string: "{dataset.bbox}"')
            feature_type_list.feature_type.append(
                FeatureTypeType(
                    name=QName(published_as.name),
                    title=[WfsTitle(value=published_as.title)],
                    default_crs=source_crs.ogc_uri,
                    output_formats=OutputFormatListType(
                        format=[
                            "application/gml+xml; version=3.2",
                            "text/xml; subtype=gml/3.2.1",
                            "text/xml; subtype=gml/3.1.1",
                            "text/xml; subtype=gml/2.1.2",
                        ]
                    ),
                    wgs84_bounding_box=[
                        Wgs84BoundingBox(
                            lower_corner=[bbox_object.minx, bbox_object.miny],
                            upper_corner=[bbox_object.maxx, bbox_object.maxy],
                        )
                    ],
                )
            )

            # TODO: Further produce Capabilities!
    wfs_capabilities = WfsCapabilitiesType(
        service_identification=service_identification,
        service_provider=service_provider,
        operations_metadata=operations_metadata,
        filter_capabilities=filter_capabilities,
        version="2.0.0",
        feature_type_list=feature_type_list,
    )
    allowed_formats = ["TEXT/XML", "APPLICATION/JSON"]
    requested_format = params.get("FORMAT", "TEXT/XML")
    if requested_format not in allowed_formats:
        requested_format = "TEXT/XML"
    if requested_format == "TEXT/XML":
        serializer = XmlSerializer()
        return HttpResponse(
            serializer.render(
                wfs_capabilities,
                ns_map={
                    "wfs": "http://www.opengis.net/wfs/2.0",
                    "xlink": "http://www.w3.org/1999/xlink",
                    "fes": "http://www.opengis.net/fes/2.0",
                    "ows": "http://www.opengis.net/ows/1.1",
                    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
                },
            ),
            content_type="text/xml",
        )
    elif requested_format == "APPLICATION/JSON":
        serializer = JsonSerializer()
        return HttpResponse(
            serializer.render(wfs_capabilities), content_type="application/json"
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
    for published_as in PublishedAsWms.objects.filter(name__in=service_params.layers):
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
            print(service_params, accessible_vector)
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
        config = Config()
        result = await redis_queue.post(job, config.job_timeout)
        return HttpResponse(result.data, result.content_type)
    elif params["SERVICE"].upper() == "WFS":
        if params["REQUEST"] == "GETCAPABILITIES":
            if params.get("VERSION", "2.0.0") == "2.0.0":
                return await sync_to_async(wfs_200_capabilities, thread_sensitive=True)(
                    request, params
                )
            else:
                return HttpResponse("Only VERSION 2.0.0 is available", 500)
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
