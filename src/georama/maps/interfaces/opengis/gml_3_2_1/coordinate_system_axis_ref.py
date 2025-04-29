from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_system_axis_property_type import (
    CoordinateSystemAxisPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateSystemAxisRef(CoordinateSystemAxisPropertyType):
    class Meta:
        name = "coordinateSystemAxisRef"
        namespace = "http://www.opengis.net/gml/3.2"
