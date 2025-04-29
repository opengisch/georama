from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.gml_3_2_1.bspline_type import BsplineType
from georama.maps.interfaces.opengis.gml_3_2_1.curve_interpolation_type import (
    CurveInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BezierType(BsplineType):
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.POLYNOMIAL_SPLINE,
        metadata={
            "type": "Attribute",
        },
    )
    is_polynomial: bool = field(
        init=False,
        default=True,
        metadata={
            "name": "isPolynomial",
            "type": "Attribute",
        },
    )
    knot_type: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
