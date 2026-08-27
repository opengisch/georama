from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinates import Coordinates
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.curve_interpolation_type import (
    CurveInterpolationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_property import (
    PointProperty,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_rep import PointRep
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pos import Pos
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pos_list import PosList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CubicSplineType(AbstractCurveSegmentType):
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
    vector_at_start: VectorType | None = field(
        default=None,
        metadata={
            "name": "vectorAtStart",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    vector_at_end: VectorType | None = field(
        default=None,
        metadata={
            "name": "vectorAtEnd",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CUBIC_SPLINE,
        metadata={
            "type": "Attribute",
        },
    )
    degree: int = field(
        init=False,
        default=3,
        metadata={
            "type": "Attribute",
        },
    )
