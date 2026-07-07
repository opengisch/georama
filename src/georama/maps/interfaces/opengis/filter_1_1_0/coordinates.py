from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.coordinates_type import (
    CoordinatesType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Coordinates(CoordinatesType):
    """
    Deprecated with GML version 3.1.0.
    """

    class Meta:
        name = "coordinates"
        namespace = "http://www.opengis.net/gml"
