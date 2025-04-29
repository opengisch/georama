from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_system_axis_property_type import (
    CoordinateSystemAxisPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesAxis(CoordinateSystemAxisPropertyType):
    class Meta:
        name = "usesAxis"
        namespace = "http://www.opengis.net/gml/3.2"
