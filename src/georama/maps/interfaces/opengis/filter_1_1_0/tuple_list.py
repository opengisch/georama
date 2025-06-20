from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.coordinates_type import (
    CoordinatesType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TupleList(CoordinatesType):
    class Meta:
        name = "tupleList"
        namespace = "http://www.opengis.net/gml"
