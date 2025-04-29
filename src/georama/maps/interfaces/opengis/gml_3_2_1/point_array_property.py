from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.point_array_property_type import (
    PointArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointArrayProperty(PointArrayPropertyType):
    class Meta:
        name = "pointArrayProperty"
        namespace = "http://www.opengis.net/gml/3.2"
