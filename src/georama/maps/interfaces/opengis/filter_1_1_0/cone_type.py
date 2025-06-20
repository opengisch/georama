from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gridded_surface_type import (
    AbstractGriddedSurfaceType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.curve_interpolation_type import (
    CurveInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConeType(AbstractGriddedSurfaceType):
    """A cone is a gridded surface given as a family of conic sections whose
    control points vary linearly.

    NOTE! A 5-point ellipse with all defining positions identical is a
    point. Thus, a truncated elliptical cone can be given as a 2x5 set
    of control points ((P1, P1, P1, P1, P1), (P2, P3, P4, P5, P6)). P1
    is the apex of the cone. P2, P3,P4, P5 and P6 are any five distinct
    points around the base ellipse of the cone. If the horizontal curves
    are circles as opposed to ellipses, the a circular cone can be
    constructed using ((P1, P1, P1),(P2, P3, P4)). The apex most not
    coinside with the other plane.
    """

    horizontal_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "horizontalCurveType",
            "type": "Attribute",
        },
    )
    vertical_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.LINEAR,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        },
    )
