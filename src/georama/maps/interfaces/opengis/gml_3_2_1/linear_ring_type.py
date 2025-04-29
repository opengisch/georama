from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_ring_type import (
    AbstractRingType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.coordinates import Coordinates
from georama.maps.interfaces.opengis.gml_3_2_1.point_property import PointProperty
from georama.maps.interfaces.opengis.gml_3_2_1.point_rep import PointRep
from georama.maps.interfaces.opengis.gml_3_2_1.pos import Pos
from georama.maps.interfaces.opengis.gml_3_2_1.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearRingType(AbstractRingType):
    pos: list[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: list[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_rep: list[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
