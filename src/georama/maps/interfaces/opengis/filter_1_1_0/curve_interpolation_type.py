from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class CurveInterpolationType(Enum):
    """
    CurveInterpolationType is a list of codes that may be used to identify the
    interpolation mechanisms specified by an application schema.
    """

    LINEAR = "linear"
    GEODESIC = "geodesic"
    CIRCULAR_ARC3_POINTS = "circularArc3Points"
    CIRCULAR_ARC2_POINT_WITH_BULGE = "circularArc2PointWithBulge"
    CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS = "circularArcCenterPointWithRadius"
    ELLIPTICAL = "elliptical"
    CLOTHOID = "clothoid"
    CONIC = "conic"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    CUBIC_SPLINE = "cubicSpline"
    RATIONAL_SPLINE = "rationalSpline"
