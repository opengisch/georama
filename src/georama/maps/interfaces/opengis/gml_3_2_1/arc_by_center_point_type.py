from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.angle_type import AngleType
from georama.maps.interfaces.opengis.gml_3_2_1.coordinates import Coordinates
from georama.maps.interfaces.opengis.gml_3_2_1.curve_interpolation_type import (
    CurveInterpolationType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.length_type import LengthType
from georama.maps.interfaces.opengis.gml_3_2_1.point_property import PointProperty
from georama.maps.interfaces.opengis.gml_3_2_1.point_rep import PointRep
from georama.maps.interfaces.opengis.gml_3_2_1.pos import Pos
from georama.maps.interfaces.opengis.gml_3_2_1.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcByCenterPointType(AbstractCurveSegmentType):
    pos: Pos | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: PointProperty | None = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_rep: PointRep | None = field(
        default=None,
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
    radius: LengthType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    start_angle: AngleType | None = field(
        default=None,
        metadata={
            "name": "startAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    end_angle: AngleType | None = field(
        default=None,
        metadata={
            "name": "endAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS,
        metadata={
            "type": "Attribute",
        },
    )
    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
            "required": True,
        },
    )
