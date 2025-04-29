from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.sc_crs_property_type import (
    CrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CrsRef(CrspropertyType):
    class Meta:
        name = "crsRef"
        namespace = "http://www.opengis.net/gml/3.2"
