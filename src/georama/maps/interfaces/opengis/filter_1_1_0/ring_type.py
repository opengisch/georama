from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_ring_type import (
    AbstractRingType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.curve_property_type import CurveMember

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RingType(AbstractRingType):
    """A Ring is used to represent a single connected component of a surface
    boundary.

    It consists of a sequence of curves connected in a cycle (an object whose boundary is empty).
    A Ring is structurally similar to a composite curve in that the endPoint of each curve in the sequence is the startPoint of the next curve in the Sequence. Since the sequence is circular, there is no exception to this rule. Each ring, like all boundaries, is a cycle and each ring is simple.
    NOTE: Even though each Ring is simple, the boundary need not be simple. The easiest case of this is where one of the interior rings of a surface is tangent to its exterior ring.

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
