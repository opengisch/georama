from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.coordinates import Coordinates
from georama.maps.interfaces.opengis.gml_3_2_1.curve_interpolation_type import (
    CurveInterpolationType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.point_property import PointProperty
from georama.maps.interfaces.opengis.gml_3_2_1.point_rep import PointRep
from georama.maps.interfaces.opengis.gml_3_2_1.pos import Pos
from georama.maps.interfaces.opengis.gml_3_2_1.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcStringType(AbstractCurveSegmentType):
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
    pos_list: PosList | None = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinates: Coordinates | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "type": "Attribute",
        },
    )
    num_arc: int | None = field(
        default=None,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        },
    )
