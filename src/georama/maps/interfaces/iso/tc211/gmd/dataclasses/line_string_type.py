from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_curve_type import (
    AbstractCurveType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinates import Coordinates
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_property import (
    PointProperty,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_rep import PointRep
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pos import Pos
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineStringType(AbstractCurveType):
    pos: list[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_property: list[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_rep: list[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pos_list: PosList | None = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinates: Coordinates | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
