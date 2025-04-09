from typing import List

from qgis_server_light.interface.qgis import BBox
from qgis_server_light.interface.qgis import Crs as QslCrs
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer

from georama.maps.interfaces.ogc.wms_1_3_0.capabilities.capabilities_1_3_0 import (
    Abstract,
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
from georama.maps.services.wms_1_3_0 import WmsOperation


class WmsGetCapabilities(WmsOperation):
    @property
    def allowed_formats(self) -> List[str]:
        return ["TEXT/XML", "APPLICATION/JSON"]

    def get_capabilities_body(self) -> WmsCapabilities:
        config = Config()
        decoder = DictDecoder()
        service = decoder.decode(config.wms_1_3_0_service_config(self.url), Service)
        capapility = decoder.decode(config.wms_1_3_0_capability_config(self.url), Capability)
        return WmsCapabilities(service=service, capability=capapility)

    @staticmethod
    def create_layer(
        name: str, title: str, description: str, crs: str, bbox: BBox, bbox_wgs84: BBox
    ) -> Layer:
        bbox_object_storage = BoundingBox(
            crs=crs,
            minx=bbox.x_min,
            maxx=bbox.x_max,
            miny=bbox.y_min,
            maxy=bbox.y_max,
        )
        ex_geographic_bounding_box_object = ExGeographicBoundingBox(
            west_bound_longitude=bbox_wgs84.x_min,
            east_bound_longitude=bbox_wgs84.x_max,
            south_bound_latitude=bbox_wgs84.y_min,
            north_bound_latitude=bbox_wgs84.y_max,
        )
        bbox_object_84 = BoundingBox(
            crs="CRS:84",
            minx=bbox_wgs84.x_min,
            maxx=bbox_wgs84.x_max,
            miny=bbox_wgs84.y_min,
            maxy=bbox_wgs84.y_max,
        )
        return Layer(
            queryable=False,
            cascaded=0,
            name=Name(value=name),
            title=Title(value=title),
            abstract=Abstract(value=description),
            crs=[Crs(crs), Crs("CRS:84")],
            ex_geographic_bounding_box=ex_geographic_bounding_box_object,
            bounding_box=[bbox_object_storage, bbox_object_84],
            # TODO: We can obtain information about available styles from passed QML
            style=[Style(name=Name("default"), title=Title("Default"))],
        )

    def get_capabilities(self) -> WmsCapabilities:
        capabilities = self.get_capabilities_body()
        for published_as in self.obtain_accessible_layers():
            dataset = published_as.bound_dataset
            source_crs = DictDecoder().decode(dataset.crs, QslCrs)
            bbox = BBox.from_string(dataset.bbox)
            bbox_wgs84 = BBox.from_string(dataset.bbox_wgs84)
            layer = self.create_layer(
                published_as.name,
                published_as.title,
                published_as.description,
                source_crs.auth_id,
                bbox,
                bbox_wgs84,
            )
            capabilities.capability.layer.layer.append(layer)

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
