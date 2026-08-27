from dataclasses import dataclass, field
from decimal import Decimal

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.clothoid_type_ref_location import (
    ClothoidTypeRefLocation,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ClothoidType(AbstractCurveSegmentType):
    """A clothoid, or Cornu's spiral, is plane curve whose curvature is a fixed
    function of its length.

    In suitably chosen co-ordinates it is given by Fresnel's integrals.
    x(t) = 0-integral-t cos(AT*T/2)dT y(t) = 0-integral-t sin(AT*T/2)dT
    This geometry is mainly used as a transition curve between curves of
    type straight line to circular arc or circular arc to circular arc.
    With this curve type it is possible to achieve a C2-continous
    transition between the above mentioned curve types. One formula for
    the Clothoid is A*A = R*t where A is constant, R is the varying
    radius of curvature along the the curve and t is the length along
    and given in the Fresnel integrals.

    :ivar ref_location:
    :ivar scale_factor: The element gives the value for the constant in
        the Fresnel's integrals.
    :ivar start_parameter: The startParameter is the arc length distance
        from the inflection point that will be the start point for this
        curve segment. This shall be lower limit used in the Fresnel
        integral and is the value of the constructive parameter of this
        curve segment at its start point. The startParameter can either
        be positive or negative. NOTE! If 0.0 (zero), lies between the
        startParameter and the endParameter of the clothoid, then the
        curve goes through the clothoid's inflection point, and the
        direction of its radius of curvature, given by the second
        derivative vector, changes sides with respect to the tangent
        vector. The term length distance for the
    :ivar end_parameter: The endParameter is the arc length distance
        from the inflection point that will be the end point for this
        curve segment. This shall be upper limit used in the Fresnel
        integral and is the value of the constructive parameter of this
        curve segment at its start point. The startParameter can either
        be positive or negative.
    """

    ref_location: ClothoidTypeRefLocation | None = field(
        default=None,
        metadata={
            "name": "refLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    scale_factor: Decimal | None = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    start_parameter: float | None = field(
        default=None,
        metadata={
            "name": "startParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    end_parameter: float | None = field(
        default=None,
        metadata={
            "name": "endParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
