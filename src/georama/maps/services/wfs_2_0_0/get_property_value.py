

import logging
from typing import List
from xml.etree.ElementTree import QName

from qgis_server_light.interface.qgis import BBox
from qgis_server_light.interface.qgis import Crs as QSL_Crs
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.serializers import JsonSerializer, XmlSerializer

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.wgs84_bounding_box import (
    Wgs84BoundingBox,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2 import (
    GetPropertyValue,
    GetPropertyValueType
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.feature_type_type import (
    FeatureTypeType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.output_format_list_type import (
    OutputFormatListType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.title import Title
from georama.maps.maps_config import Config
from georama.maps.services.wfs_2_0_0 import WfsOperation


class WgsGetPropertyValue(WfsOperation):
    @property
    def allowed_formats(self) -> List[str]:
        return ["TEXT/XML", "APPLICATION/JSON"]
        # ? add "application/gml+xml; version=3.2", "text/xml; subtype=gml/3.2.1", "text/xml; subtype=gml/3.1.1", "text/xml; subtype=gml/2.1.2",

    def get_property_value(self) -> GetPropertyValue:
        raise NotImplementedError()

    @staticmethod
    def render_xml(capabilities: GetPropertyValue) -> str:
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

    # remove render_json?
    @staticmethod
    def render_json(capabilities: GetPropertyValue) -> str:
        serializer = JsonSerializer()
        return serializer.render(capabilities)

    def render(self, requested_format: str, capabilities: GetPropertyValue) -> str | None:
        if requested_format == "TEXT/XML":
            return self.render_xml(capabilities)
        elif requested_format == "APPLICATION/JSON":
            return self.render_json(capabilities)
        else:
            logging.debug("No matching Format was found.")
            return None

