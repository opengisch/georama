from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.coord import Coord
from georama.maps.interfaces.opengis.filter_1_1_0.coordinates import Coordinates
from georama.maps.interfaces.opengis.filter_1_1_0.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointType(AbstractGeometricPrimitiveType):
    """
    A Point is defined by a single coordinate tuple.
    """

    pos_or_coordinates_or_coord: Pos | Coordinates | Coord | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "pos",
                    "type": Pos,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "coordinates",
                    "type": Coordinates,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "coord",
                    "type": Coord,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
