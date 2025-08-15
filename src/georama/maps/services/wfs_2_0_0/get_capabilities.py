import logging
from typing import List
from xml.etree.ElementTree import QName

from qgis_server_light.interface.qgis import BBox
from qgis_server_light.interface.qgis import Crs as QSL_Crs
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer

from georama.maps.interfaces.ogc.wfs_2_0_0 import (
    DefaultCrs,
    FeatureTypeType,
    MetadataUrltype,
    OutputFormatListType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0 import Title2 as Title
from georama.maps.interfaces.ogc.wfs_2_0_0 import WfsCapabilities, Wgs84BoundingBox
from georama.maps.maps_config import Config
from georama.maps.services.wfs_2_0_0 import WfsOperation


class WfsGetCapabilities(WfsOperation):
    @property
    def allowed_formats(self) -> List[str]:
        return ["TEXT/XML", "APPLICATION/JSON"]

    def get_capabilities_body(self) -> WfsCapabilities:
        config = Config()
        return config.wfs_2_0_0_capabilities_config(self.url)

    @staticmethod
    def create_feature_type(name: str, title: str, crs: str, bbox: BBox, url: str):
        return FeatureTypeType(
            name=QName(name),
            title=[Title(value=title)],
            default_crs_or_other_crs_or_no_crs=[DefaultCrs(value=crs)],
            output_formats=OutputFormatListType(
                format=["application/gml+xml; version=3.2", "text/xml; subtype=gml/3.2.1"]
            ),
            wgs84_bounding_box=[
                Wgs84BoundingBox(
                    lower_corner=[bbox.x_min, bbox.y_min],
                    upper_corner=[bbox.x_max, bbox.y_max],
                )
            ],
            metadata_url=[
                MetadataUrltype(href=f"{url}request=GetMetadata&layer={name.split(':')[1]}")
            ],
        )

    def get_capabilities(self) -> WfsCapabilities:
        wfs_capabilities = self.get_capabilities_body()
        for published_as in self.obtain_accessible_layers():
            dataset = published_as.vector_dataset
            source_crs = DictDecoder().decode(dataset.crs, QSL_Crs)
            bbox = BBox.from_string(dataset.bbox_wgs84)
            wfs_capabilities.feature_type_list.feature_type.append(
                self.create_feature_type(
                    f"{self.own_namespace}:{published_as.name}",
                    published_as.title,
                    source_crs.ogc_uri,
                    bbox,
                    self.url,
                )
            )
        return wfs_capabilities

    @staticmethod
    def render_xml(capabilities: WfsCapabilities) -> str:
        serializer = XmlSerializer()
        return serializer.render(
            capabilities,
            ns_map={
                "wfs": "http://www.opengis.net/wfs/2.0",
                "xlink": "http://www.w3.org/1999/xlink",
                "fes": "http://www.opengis.net/fes/2.0",
                "ows": "http://www.opengis.net/ows/1.1",
                "xsi": "http://www.w3.org/2001/XMLSchema-instance",
            },
        )

    @staticmethod
    def render_json(capabilities: WfsCapabilities) -> str:
        serializer = JsonSerializer()
        return serializer.render(capabilities)

    def render(self, requested_format: str, capabilities: WfsCapabilities) -> str | None:
        if requested_format == "TEXT/XML":
            return self.render_xml(capabilities)
        elif requested_format == "APPLICATION/JSON":
            return self.render_json(capabilities)
        else:
            logging.debug("No matching Format was found.")
            return None
