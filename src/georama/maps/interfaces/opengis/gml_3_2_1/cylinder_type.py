from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_gridded_surface_type import (
    AbstractGriddedSurfaceType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.curve_interpolation_type import (
    CurveInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CylinderType(AbstractGriddedSurfaceType):
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
