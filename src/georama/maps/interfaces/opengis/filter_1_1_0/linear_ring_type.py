from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_ring_type import (
    AbstractRingType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.coord import Coord
from georama.maps.interfaces.opengis.filter_1_1_0.coordinates import Coordinates
from georama.maps.interfaces.opengis.filter_1_1_0.point_property import PointProperty
from georama.maps.interfaces.opengis.filter_1_1_0.point_rep import PointRep
from georama.maps.interfaces.opengis.filter_1_1_0.pos import Pos
from georama.maps.interfaces.opengis.filter_1_1_0.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearRingType(AbstractRingType):
    """
    A LinearRing is defined by four or more coordinate tuples, with linear
    interpolation between them; the first and last coordinates must be coincident.
    """

    choice_1: list[Pos | PointProperty | PointRep | PosList | Coordinates | Coord] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "pos",
                        "type": Pos,
                        "namespace": "http://www.opengis.net/gml",
                    },
                    {
                        "name": "pointProperty",
                        "type": PointProperty,
                        "namespace": "http://www.opengis.net/gml",
                    },
                    {
                        "name": "pointRep",
                        "type": PointRep,
                        "namespace": "http://www.opengis.net/gml",
                    },
                    {
                        "name": "posList",
                        "type": PosList,
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
    )
