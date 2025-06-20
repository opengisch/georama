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
class CubicSplineType(AbstractCurveSegmentType):
    """Cubic splines are similar to line strings in that they are a sequence of
    segments each with its own defining function.

    A cubic spline uses the control points and a set of derivative parameters to define a piecewise 3rd degree polynomial interpolation. Unlike line-strings, the parameterization by arc length is not necessarily still a polynomial.
    The function describing the curve must be C2, that is, have a continuous 1st and 2nd derivative at all points, and pass through the controlPoints in the order given. Between the control points, the curve segment is defined by a cubic polynomial. At each control point, the polynomial changes in such a manner that the 1st and 2nd derivative vectors are the same from either side. The control parameters record must contain vectorAtStart, and vectorAtEnd which are the unit tangent vectors at controlPoint[1] and controlPoint[n] where n = controlPoint.count.
    Note: only the direction of the vectors is relevant, not their length.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    :ivar vector_at_start: "vectorAtStart" is the unit tangent vector at
        the start point of the spline.
    :ivar vector_at_end: "vectorAtEnd" is the unit tangent vector at the
        end point of the spline.
    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For a CubicSpline
        the interpolation is fixed as "cubicSpline".
    :ivar degree: The degree for a cubic spline is "3".
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
    vector_at_start: Optional[VectorType] = field(
        default=None,
        metadata={
            "name": "vectorAtStart",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    vector_at_end: Optional[VectorType] = field(
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
