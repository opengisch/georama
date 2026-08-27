from dataclasses import dataclass, field

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

    :ivar choice:
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

    choice: list[Pos | PointProperty | PointRep | PosList | Coordinates] = field(
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
            ),
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
    num_arc: int | None = field(
        default=None,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        },
    )
