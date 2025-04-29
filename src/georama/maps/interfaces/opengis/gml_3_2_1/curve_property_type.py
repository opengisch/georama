from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.abstract_curve_type import (
    AbstractCurveType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.abstract_ring_type import (
    AbstractRingType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType
from georama.maps.interfaces.opengis.gml_3_2_1.arc import Arc
from georama.maps.interfaces.opengis.gml_3_2_1.arc_by_bulge import ArcByBulge
from georama.maps.interfaces.opengis.gml_3_2_1.arc_by_center_point import (
    ArcByCenterPoint,
)
from georama.maps.interfaces.opengis.gml_3_2_1.arc_string import ArcString
from georama.maps.interfaces.opengis.gml_3_2_1.arc_string_by_bulge import (
    ArcStringByBulge,
)
from georama.maps.interfaces.opengis.gml_3_2_1.bezier import Bezier
from georama.maps.interfaces.opengis.gml_3_2_1.bspline import Bspline
from georama.maps.interfaces.opengis.gml_3_2_1.circle import Circle
from georama.maps.interfaces.opengis.gml_3_2_1.circle_by_center_point import (
    CircleByCenterPoint,
)
from georama.maps.interfaces.opengis.gml_3_2_1.clothoid import Clothoid
from georama.maps.interfaces.opengis.gml_3_2_1.cubic_spline import CubicSpline
from georama.maps.interfaces.opengis.gml_3_2_1.geodesic import Geodesic
from georama.maps.interfaces.opengis.gml_3_2_1.geodesic_string import GeodesicString
from georama.maps.interfaces.opengis.gml_3_2_1.length_type import LengthType
from georama.maps.interfaces.opengis.gml_3_2_1.line_string import LineString
from georama.maps.interfaces.opengis.gml_3_2_1.line_string_segment import (
    LineStringSegment,
)
from georama.maps.interfaces.opengis.gml_3_2_1.linear_ring import LinearRing
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType
from georama.maps.interfaces.opengis.gml_3_2_1.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CurvePropertyType:
    """A property that has a curve as its value domain may either be an appropriate
    geometry element encapsulated in an element of this type or an XLink reference
    to a remote geometry element (where remote includes geometry elements located
    elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """

    composite_curve: Optional["CompositeCurve"] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientable_curve: Optional["OrientableCurve"] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    curve: Optional["Curve"] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ring: Optional["Ring"] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class OffsetCurveType(AbstractCurveSegmentType):
    offset_base: Optional[CurvePropertyType] = field(
        default=None,
        metadata={
            "name": "offsetBase",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    distance: Optional[LengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    ref_direction: Optional[VectorType] = field(
        default=None,
        metadata={
            "name": "refDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class BaseCurve(CurvePropertyType):
    """The property baseCurve references or contains the base curve, i.e. it either
    references the base curve via the XLink-attributes or contains the curve
    element.

    A curve element is any element which is substitutable for
    AbstractCurve. The base curve has positive orientation.
    """

    class Meta:
        name = "baseCurve"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveMember(CurvePropertyType):
    class Meta:
        name = "curveMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompositeCurveType(AbstractCurveType):
    curve_member: list[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class OffsetCurve(OffsetCurveType):
    """An offset curve is a curve at a constant distance from the basis curve.

    offsetBase is the base curve from which this curve is defined as an
    offset. distance and refDirection have the same meaning as specified
    in ISO 19107:2003, 6.4.23. The content model follows the general
    pattern for the encoding of curve segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OrientableCurveType(AbstractCurveType):
    base_curve: Optional[BaseCurve] = field(
        default=None,
        metadata={
            "name": "baseCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    orientation: str = field(
        default="+",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RingType(AbstractRingType):
    curve_member: list[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class CompositeCurve(CompositeCurveType):
    """A gml:CompositeCurve is represented by a sequence of (orientable) curves
    such that each curve in the sequence terminates at the start point of the
    subsequent curve in the list.

    curveMember references or contains inline one curve in the composite
    curve. The curves are contiguous, the collection of curves is
    ordered. Therefore, if provided, the aggregationType attribute shall
    have the value "sequence".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveSegmentArrayPropertyType:
    """
    Gml:CurveSegmentArrayPropertyType is a container for an array of curve
    segments.
    """

    geodesic: list[Geodesic] = field(
        default_factory=list,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    geodesic_string: list[GeodesicString] = field(
        default_factory=list,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    clothoid: list[Clothoid] = field(
        default_factory=list,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    offset_curve: list[OffsetCurve] = field(
        default_factory=list,
        metadata={
            "name": "OffsetCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    bezier: list[Bezier] = field(
        default_factory=list,
        metadata={
            "name": "Bezier",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    bspline: list[Bspline] = field(
        default_factory=list,
        metadata={
            "name": "BSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    cubic_spline: list[CubicSpline] = field(
        default_factory=list,
        metadata={
            "name": "CubicSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    circle_by_center_point: list[CircleByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    arc_by_center_point: list[ArcByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    arc_by_bulge: list[ArcByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    arc_string_by_bulge: list[ArcStringByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcStringByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    circle: list[Circle] = field(
        default_factory=list,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    arc: list[Arc] = field(
        default_factory=list,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    arc_string: list[ArcString] = field(
        default_factory=list,
        metadata={
            "name": "ArcString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    line_string_segment: list[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )


@dataclass
class OrientableCurve(OrientableCurveType):
    """OrientableCurve consists of a curve and an orientation.

    If the orientation is "+", then the OrientableCurve is identical to
    the baseCurve. If the orientation is "-", then the OrientableCurve
    is related to another AbstractCurve with a parameterization that
    reverses the sense of the curve traversal.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Ring(RingType):
    """A ring is used to represent a single connected component of a surface
    boundary as specified in ISO 19107:2003, 6.3.6.

    Every gml:curveMember references or contains one curve, i.e. any
    element which is substitutable for gml:AbstractCurve. In the context
    of a ring, the curves describe the boundary of the surface. The
    sequence of curves shall be contiguous and connected in a cycle. If
    provided, the aggregationType attribute shall have the value
    "sequence".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Segments(CurveSegmentArrayPropertyType):
    """This property element contains a list of curve segments.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "segments"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveType(AbstractCurveType):
    segments: Optional[Segments] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class Curve(CurveType):
    """A curve is a 1-dimensional primitive.

    Curves are continuous, connected, and have a measurable length in
    terms of the coordinate system. A curve is composed of one or more
    curve segments. Each curve segment within a curve may be defined
    using a different interpolation method. The curve segments are
    connected to one another, with the end point of each segment except
    the last being the start point of the next segment in the segment
    list. The orientation of the curve is positive. The element segments
    encapsulates the segments of the curve.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
