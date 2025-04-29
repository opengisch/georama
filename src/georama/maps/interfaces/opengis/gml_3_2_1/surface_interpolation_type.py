from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class SurfaceInterpolationType(Enum):
    """
    Gml:SurfaceInterpolationType is a list of codes that may be used to identify
    the interpolation mechanisms specified by an application schema.
    """

    NONE = "none"
    PLANAR = "planar"
    SPHERICAL = "spherical"
    ELLIPTICAL = "elliptical"
    CONIC = "conic"
    TIN = "tin"
    PARAMETRIC_CURVE = "parametricCurve"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    RATIONAL_SPLINE = "rationalSpline"
    TRIANGULATED_SPLINE = "triangulatedSpline"
