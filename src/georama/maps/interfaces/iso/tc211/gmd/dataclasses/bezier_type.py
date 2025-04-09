from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.bspline_type import BsplineType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.curve_interpolation_type import (
    CurveInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


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
        metadata={
            "type": "Ignore",
        },
    )
