from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_system_property_type import (
    CoordinateSystemPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesCs(CoordinateSystemPropertyType):
    class Meta:
        name = "usesCS"
        namespace = "http://www.opengis.net/gml/3.2"
