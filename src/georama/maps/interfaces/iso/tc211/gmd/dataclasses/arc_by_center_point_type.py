from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.angle_type import AngleType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinates import Coordinates
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.curve_interpolation_type import (
    CurveInterpolationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.length_type import LengthType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_property import (
    PointProperty,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_rep import PointRep
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pos import Pos
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcByCenterPointType(AbstractCurveSegmentType):
    pos: Pos | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_property: PointProperty | None = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_rep: PointRep | None = field(
        default=None,
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
    radius: LengthType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    start_angle: AngleType | None = field(
        default=None,
        metadata={
            "name": "startAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    end_angle: AngleType | None = field(
        default=None,
        metadata={
            "name": "endAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
