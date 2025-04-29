from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.direction_property_type import (
    DirectionPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Direction(DirectionPropertyType):
    """
    The property gml:direction is intended as a pre-defined property expressing a
    direction to be assigned to features defined in a GML application schema.
    """

    class Meta:
        name = "direction"
        namespace = "http://www.opengis.net/gml/3.2"
