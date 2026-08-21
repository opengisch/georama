import logging

from qgis_server_light.interface.common import BBox
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer

from georama.maps.interfaces.ogc.wms_1_3_0.capabilities.capabilities_1_3_0 import (
    Abstract,
    BoundingBox,
    Crs,
    ExGeographicBoundingBox,
    Format,
    Layer,
    LegendUrl,
    Name,
    OnlineResource,
    Style,
    Title,
    WmsCapabilities,
)
from georama.maps.maps_config import Config
from georama.maps.services.wms_1_3_0 import WmsOperation


class WmsGetCapabilities(WmsOperation):
    @property
    def allowed_formats(self) -> list[str]:
        return ["TEXT/XML", "APPLICATION/JSON"]

    def get_capabilities_body(self) -> WmsCapabilities:
        config = Config()
        decoder_config = ParserConfig(
            fail_on_unknown_properties=False, fail_on_unknown_attributes=False
        )
        DictDecoder(decoder_config)
        service = config.wms_1_3_0_service_config(self.url)
        capapility = config.wms_1_3_0_capability_config(self.url)
        return WmsCapabilities(service=service, capability=capapility)

    @staticmethod
    def create_layer(
        name: str,
        title: str,
        description: str,
        crs: str,
        bbox: BBox,
        bbox_wgs84: BBox,
        styles: list[str],
        queryable: bool,
    ) -> Layer:
        layer_crs_bboxes = {
            crs: BoundingBox(
                crs=crs,
                minx=bbox.x_min,
                maxx=bbox.x_max,
                miny=bbox.y_min,
                maxy=bbox.y_max,
            ),
            WmsGetCapabilities.crs_84: ExGeographicBoundingBox(
                west_bound_longitude=bbox_wgs84.x_min,
                east_bound_longitude=bbox_wgs84.x_max,
                south_bound_latitude=bbox_wgs84.y_min,
                north_bound_latitude=bbox_wgs84.y_max,
            ),
        }
        if WmsGetCapabilities.crs_4326 not in layer_crs_bboxes:
            layer_crs_bboxes[WmsGetCapabilities.crs_4326] = BoundingBox(
                crs="EPSG:4326",
                minx=bbox_wgs84.y_min,
                maxx=bbox_wgs84.y_max,
                miny=bbox_wgs84.x_min,
                maxy=bbox_wgs84.x_max,
            )

        return Layer(
            # we use a 0/1 instead True/False here since this also conforms
            # to Chapter 7.2.4.7.1 in
            # https://github.com/opengisch/georama/blob/master/tests/maps/resources/wms/06-042_OpenGIS_Web_Map_Service_WMS_Implementation_Specification.pdf and opens  # noqa: E501
            # compatibility with older versions of WMS spec
            queryable=1 if queryable else 0,
            opaque=0,
            no_subsets=0,
            cascaded=0,
            name=Name(value=name),
            title=Title(value=title),
            abstract=Abstract(value=description),
            crs=[Crs(key) for key in layer_crs_bboxes],
            ex_geographic_bounding_box=layer_crs_bboxes[WmsGetCapabilities.crs_84],
            bounding_box=[
                bbox for _, bbox in layer_crs_bboxes.items() if isinstance(bbox, BoundingBox)
            ],
            # TODO: We can obtain information about available styles from passed QML
            style=[
                Style(
                    name=Name(style_name),
                    title=Title(style_name.title()),
                    legend_url=[
                        LegendUrl(
                            format=Format("image/png"),
                            online_resource=OnlineResource(
                                href="?SERVICE=WMS&REQUEST=GETLEGENDGRAPHIC&VERSION=1.3.0&"
                                f"LAYERS={name}&STYLES={style_name}&FORMAT=image%2Fpng",
                            ),
                        )
                    ],
                )
                for style_name in styles
            ],
        )

    def get_capabilities(self) -> WmsCapabilities:
        capabilities = self.get_capabilities_body()
        for published_as in self.obtain_accessible_layers():
            dataset = published_as.bound_dataset
            styles = dataset.styles_to_qsl
            style_names = [style.name for style in styles]
            if "default" not in style_names:
                logging.debug(
                    f"No Style named 'default' was existing in the configuration of the\n"
                    f"  dataset {dataset.name} ({dataset.id}), the first style"
                    f" in the list of defined\n"
                    f"  styles was added as default style."
                )
                style_names.insert(0, "default")
            extent = BBox.from_string(published_as.extent)
            extent_wgs84 = BBox.from_string(published_as.extent_wgs84)
            layer = self.create_layer(
                published_as.name,
                published_as.title,
                published_as.description,
                dataset.crs_to_qsl.auth_id,
                extent,
                extent_wgs84,
                style_names,
                published_as.is_queryable,
            )
            capabilities.capability.layer.layer.append(layer)
        # we use a 0/1 instead True/False here since this also conforms to Chapter 7.2.4.7.1 in
        # https://github.com/opengisch/georama/blob/master/tests/maps/resources/wms/06-042_OpenGIS_Web_Map_Service_WMS_Implementation_Specification.pdf and opens  # noqa: E501
        # compatibility with older versions of WMS spec
        capabilities.capability.layer.queryable = 0
        capabilities.capability.layer.opaque = 0
        capabilities.capability.layer.no_subsets = 0
        return capabilities

    @staticmethod
    def render_xml(capabilities: WmsCapabilities) -> str:
        serializer = XmlSerializer()
        return serializer.render(
            capabilities,
            ns_map={
                None: "http://www.opengis.net/wms",
                "xlink": "http://www.w3.org/1999/xlink",
            },
        )

    @staticmethod
    def render_json(capabilities: WmsCapabilities) -> str:
        serializer = JsonSerializer()
        return serializer.render(capabilities)
