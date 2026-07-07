from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cubic_spline_type import (
    CubicSplineType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CubicSpline(CubicSplineType):
    """The number of control points shall be at least three.

    vectorAtStart is the unit tangent vector at the start point of the
    spline. vectorAtEnd is the unit tangent vector at the end point of
    the spline. Only the direction of the vectors shall be used to
    determine the shape of the cubic spline, not their length.
    interpolation is fixed as "cubicSpline". degree shall be the degree
    of the polynomial used for the interpolation in this spline.
    Therefore the degree for a cubic spline is fixed to "3". The content
    model follows the general pattern for the encoding of curve
    segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
