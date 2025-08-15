from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gridded_surface_type import (
    AbstractGriddedSurfaceType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.curve_interpolation_type import (
    CurveInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CylinderType(AbstractGriddedSurfaceType):
    """A cylinder is a gridded surface given as a family of circles whose positions
    vary along a set of parallel lines, keeping the cross sectional horizontal
    curves of a constant shape.

    NOTE! Given the same working assumptions as in the previous note, a
    Cylinder can be given by two circles, giving us the control points
    of the form ((P1, P2, P3),(P4, P5, P6)).
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
