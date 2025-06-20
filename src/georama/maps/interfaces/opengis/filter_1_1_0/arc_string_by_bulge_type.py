from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.coordinates import Coordinates
from georama.maps.interfaces.opengis.filter_1_1_0.curve_interpolation_type import (
    CurveInterpolationType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.point_property import PointProperty
from georama.maps.interfaces.opengis.filter_1_1_0.point_rep import PointRep
from georama.maps.interfaces.opengis.filter_1_1_0.pos import Pos
from georama.maps.interfaces.opengis.filter_1_1_0.pos_list import PosList
from georama.maps.interfaces.opengis.filter_1_1_0.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcStringByBulgeType(AbstractCurveSegmentType):
    """This variant of the arc computes the mid points of the arcs instead of
    storing the coordinates directly.

    The control point sequence consists of the start and end points of
    each arc plus the bulge.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    :ivar bulge: The bulge controls the offset of each arc's midpoint.
        The "bulge" is the real number multiplier for the normal that
        determines the offset direction of the midpoint of each arc. The
        length of the bulge sequence is exactly 1 less than the length
        of the control point array, since a bulge is needed for each
        pair of adjacent points in the control point array. The bulge is
        not given by a distance, since it is simply a multiplier for the
        normal. The midpoint of the resulting arc is given by: midPoint
        = ((startPoint + endPoint)/2.0) + bulge*normal
    :ivar normal: The attribute "normal" is a vector normal
        (perpendicular) to the chord of the arc, the line joining the
        first and last point of the arc. In a 2D coordinate system,
        there are only two possible directions for the normal, and it is
        often given as a signed real, indicating its length, with a
        positive sign indicating a left turn angle from the chord line,
        and a negative sign indicating a right turn from the chord. In
        3D, the normal determines the plane of the arc, along with the
        start and endPoint of the arc. The normal is usually a unit
        vector, but this is not absolutely necessary. If the normal is a
        zero vector, the geometric object becomes equivalent to the
        straight line between the two end points. The length of the
        normal sequence is exactly the same as for the bulge sequence, 1
        less than the control point sequence length.
    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For an
        ArcStringByBulge the interpolation is fixed as
        "circularArc2PointWithBulge".
    :ivar num_arc: The number of arcs in the arc string can be
        explicitly stated in this attribute. The number of control
        points in the arc string must be numArc + 1.
    """

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
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bulge: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    normal: list[VectorType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC2_POINT_WITH_BULGE,
        metadata={
            "type": "Attribute",
        },
    )
    num_arc: Optional[int] = field(
        default=None,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        },
    )
