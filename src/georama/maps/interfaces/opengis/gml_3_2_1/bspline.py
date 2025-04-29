from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.bspline_type import BsplineType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Bspline(BsplineType):
    """A B-Spline is a piecewise parametric polynomial or rational curve described
    in terms of control points and basis functions as specified in ISO 19107:2003,
    6.4.30.

    Therefore, interpolation may be either "polynomialSpline" or
    "rationalSpline" depending on the interpolation type; default is
    "polynomialSpline". degree shall be the degree of the polynomial
    used for interpolation in this spline. knot shall be the sequence of
    distinct knots used to define the spline basis functions (see ISO
    19107:2003, 6.4.26.2). The attribute isPolynomial shall be set to
    "true" if this is a polynomial spline (see ISO 19107:2003,
    6.4.30.5). The attribute knotType shall provide the type of knot
    distribution used in defining this spline (see ISO 19107:2003,
    6.4.30.4). The content model follows the general pattern for the
    encoding of curve segments.
    """

    class Meta:
        name = "BSpline"
        namespace = "http://www.opengis.net/gml/3.2"
