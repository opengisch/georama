from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.cubic_spline_type import (
    CubicSplineType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CubicSpline(CubicSplineType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
