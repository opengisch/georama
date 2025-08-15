from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.multi_solid_property_type import (
    MultiSolidPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSolidProperty(MultiSolidPropertyType):
    class Meta:
        name = "multiSolidProperty"
        namespace = "http://www.opengis.net/gml/3.2"
