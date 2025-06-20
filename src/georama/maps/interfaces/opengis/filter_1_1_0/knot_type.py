from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class KnotType:
    """
    A knot is a breakpoint on a piecewise spline curve.

    :ivar value: The property "value" is the value of the parameter at
        the knot of the spline. The sequence of knots shall be a non-
        decreasing sequence. That is, each knot's value in the sequence
        shall be equal to or greater than the previous knot's value. The
        use of equal consecutive knots is normally handled using the
        multiplicity.
    :ivar multiplicity: The property "multiplicity" is the multiplicity
        of this knot used in the definition of the spline (with the same
        weight).
    :ivar weight: The property "weight" is the value of the averaging
        weight used for this knot of the spline.
    """

    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    multiplicity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    weight: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
