from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinates_type import (
    CoordinatesType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Coordinates(CoordinatesType):
    class Meta:
        name = "coordinates"
        namespace = "http://www.opengis.net/gml"
