from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.direction_property_type import (
    DirectionPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Direction(DirectionPropertyType):
    class Meta:
        name = "direction"
        namespace = "http://www.opengis.net/gml"
