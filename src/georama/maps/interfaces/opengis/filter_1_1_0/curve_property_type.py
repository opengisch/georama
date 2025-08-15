from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_curve_type import (
    AbstractCurveType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.arc import Arc
from georama.maps.interfaces.opengis.filter_1_1_0.arc_by_bulge import ArcByBulge
from georama.maps.interfaces.opengis.filter_1_1_0.arc_by_center_point import (
    ArcByCenterPoint,
)
from georama.maps.interfaces.opengis.filter_1_1_0.arc_string import ArcString
from georama.maps.interfaces.opengis.filter_1_1_0.arc_string_by_bulge import (
    ArcStringByBulge,
)
from georama.maps.interfaces.opengis.filter_1_1_0.bezier import Bezier
from georama.maps.interfaces.opengis.filter_1_1_0.bspline import Bspline
from georama.maps.interfaces.opengis.filter_1_1_0.circle import Circle
from georama.maps.interfaces.opengis.filter_1_1_0.circle_by_center_point import (
    CircleByCenterPoint,
)
from georama.maps.interfaces.opengis.filter_1_1_0.clothoid import Clothoid
from georama.maps.interfaces.opengis.filter_1_1_0.cubic_spline import CubicSpline
from georama.maps.interfaces.opengis.filter_1_1_0.geodesic import Geodesic
from georama.maps.interfaces.opengis.filter_1_1_0.geodesic_string import GeodesicString
from georama.maps.interfaces.opengis.filter_1_1_0.length_type import LengthType
from georama.maps.interfaces.opengis.filter_1_1_0.line_string import LineString
from georama.maps.interfaces.opengis.filter_1_1_0.line_string_segment import (
    LineStringSegment,
)
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.sign_type import SignType
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType
from georama.maps.interfaces.opengis.filter_1_1_0.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CurvePropertyType:
    """A property that has a curve as its value domain can either be an appropriate
    geometry element encapsulated in an element of this type or an XLink reference
    to a remote geometry element (where remote includes geometry elements located
    elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """

    choice: Optional[Union["OrientableCurve", "Curve", "CompositeCurve", LineString]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OrientableCurve",
                    "type": ForwardRef("OrientableCurve"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Curve",
                    "type": ForwardRef("Curve"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeCurve",
                    "type": ForwardRef("CompositeCurve"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class OffsetCurveType(AbstractCurveSegmentType):
    """An offset curve is a curve at a constant distance from the basis curve.

    They can be useful as a cheap and simple alternative to constructing
    curves that are offsets by definition.

    :ivar offset_base: offsetBase is a reference to thecurve from which
        this curve is define as an offset.
    :ivar distance: distance is the distance at which the offset curve
        is generated from the basis curve. In 2D systems, positive
        distances are to be to the left of the basis curve, and the
        negative distances are to be to the right of the basis curve.
    :ivar ref_direction: refDistance is used to define the vector
        direction of the offset curve from the basis curve. It can be
        omitted in the 2D case, where the distance can be positive or
        negative. In that case, distance defines left side (positive
        distance) or right side (negative distance) with respect to the
        tangent to the basis curve. In 3D the basis curve shall have a
        well defined tangent direction for every point. The offset curve
        at any point in 3D, the basis curve shall have a well-defined
        tangent direction for every point. The offset curve at any point
        (parameter) on the basis curve c is in the direction -   -   -
        - s = v x t  where  v = c.refDirection() and - t = c.tangent() -
        For the offset direction to be well-defined, v shall not on any
        point of the curve be in the same, or opposite, direction as -
        t. The default value of the refDirection shall be the local co-
        ordinate axis vector for elevation, which indicates up for the
        curve in a geographic sense. NOTE! If the refDirection is the
        positive tangent to the local elevation axis ("points upward"),
        then the offset vector points to the left of the curve when
        viewed from above.
    """

    offset_base: Optional[CurvePropertyType] = field(
        default=None,
        metadata={
            "name": "offsetBase",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    distance: Optional[LengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    ref_direction: Optional[VectorType] = field(
        default=None,
        metadata={
            "name": "refDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class BaseCurve(CurvePropertyType):
    """This property element either references a curve via the XLink-attributes or
    contains the curve element.

    A curve element is any element which is substitutable for "_Curve".
    """

    class Meta:
        name = "baseCurve"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CurveMember(CurvePropertyType):
    """This property element either references a curve via the XLink-attributes or
    contains the curve element.

    A curve element is any element which is substitutable for "_Curve".
    """

    class Meta:
        name = "curveMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CompositeCurveType(AbstractCurveType):
    """
    A CompositeCurve is defined by a sequence of (orientable) curves such that the
    each curve in the sequence terminates at the start point of the subsequent
    curve in the list.

    :ivar curve_member: This element references or contains one curve in
        the composite curve. The curves are contiguous, the collection
        of curves is ordered. NOTE: This definition allows for a nested
        structure, i.e. a CompositeCurve may use, for example, another
        CompositeCurve as a curve member.
    """

    curve_member: list[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )


@dataclass
class OffsetCurve(OffsetCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class OrientableCurveType(AbstractCurveType):
    """OrientableCurve consists of a curve and an orientation.

    If the orientation is "+", then the OrientableCurve is identical to
    the baseCurve. If the orientation is "-", then the OrientableCurve
    is related to another _Curve with a parameterization that reverses
    the sense of the curve traversal.

    :ivar base_curve: References or contains the base curve (positive
        orientation). NOTE: This definition allows for a nested
        structure, i.e. an OrientableCurve may use another
        OrientableCurve as its base curve.
    :ivar orientation: If the orientation is "+", then the
        OrientableCurve is identical to the baseCurve. If the
        orientation is "-", then the OrientableCurve is related to
        another _Curve with a parameterization that reverses the sense
        of the curve traversal. "+" is the default value.
    """

    base_curve: Optional[BaseCurve] = field(
        default=None,
        metadata={
            "name": "baseCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    orientation: SignType = field(
        default=SignType.PLUS_SIGN,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CompositeCurve(CompositeCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class CurveSegmentArrayPropertyType:
    """
    A container for an array of curve segments.
    """

    choice: list[
        Union[
            Bezier,
            Bspline,
            CubicSpline,
            Geodesic,
            GeodesicString,
            Clothoid,
            OffsetCurve,
            CircleByCenterPoint,
            ArcByCenterPoint,
            ArcByBulge,
            ArcStringByBulge,
            Circle,
            Arc,
            ArcString,
            LineStringSegment,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Bezier",
                    "type": Bezier,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "BSpline",
                    "type": Bspline,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CubicSpline",
                    "type": CubicSpline,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Geodesic",
                    "type": Geodesic,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeodesicString",
                    "type": GeodesicString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Clothoid",
                    "type": Clothoid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OffsetCurve",
                    "type": OffsetCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CircleByCenterPoint",
                    "type": CircleByCenterPoint,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ArcByCenterPoint",
                    "type": ArcByCenterPoint,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ArcByBulge",
                    "type": ArcByBulge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ArcStringByBulge",
                    "type": ArcStringByBulge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Circle",
                    "type": Circle,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Arc",
                    "type": Arc,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ArcString",
                    "type": ArcString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LineStringSegment",
                    "type": LineStringSegment,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )


@dataclass
class OrientableCurve(OrientableCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Segments(CurveSegmentArrayPropertyType):
    """This property element contains a list of curve segments.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "segments"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CurveType(AbstractCurveType):
    """Curve is a 1-dimensional primitive.

    Curves are continuous, connected, and have a measurable length in
    terms of the coordinate system. A curve is composed of one or more
    curve segments. Each curve segment within a curve may be defined
    using a different interpolation method. The curve segments are
    connected to one another, with the end point of each segment except
    the last being the start point of the next segment in the segment
    list. The orientation of the curve is positive.

    :ivar segments: This element encapsulates the segments of the curve.
    """

    segments: Optional[Segments] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class Curve(CurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
