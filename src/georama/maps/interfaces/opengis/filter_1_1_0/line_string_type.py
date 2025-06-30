from dataclasses import dataclass, field
from typing import Union

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_curve_type import (
    AbstractCurveType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.coord import Coord
from georama.maps.interfaces.opengis.filter_1_1_0.coordinates import Coordinates
from georama.maps.interfaces.opengis.filter_1_1_0.point_property import PointProperty
from georama.maps.interfaces.opengis.filter_1_1_0.point_rep import PointRep
from georama.maps.interfaces.opengis.filter_1_1_0.pos import Pos
from georama.maps.interfaces.opengis.filter_1_1_0.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineStringType(AbstractCurveType):
    """A LineString is a special curve that consists of a single segment with
    linear interpolation.

    It is defined by two or more coordinate tuples, with linear
    interpolation between them. It is backwards compatible with the
    LineString of GML 2, GM_LineString of ISO 19107 is implemented by
    LineStringSegment.
    """

    choice_1: list[Union[Pos, PointProperty, PointRep, Coord, PosList, Coordinates]] = field(
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
                    "name": "coord",
                    "type": Coord,
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
            ),
        },
    )
