from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.bezier_type import BezierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Bezier(BezierType):
    """Bezier curves are polynomial splines that use Bezier or Bernstein
    polynomials for interpolation purposes.

    It is a special case of the B-Spline curve with two knots. degree
    shall be the degree of the polynomial used for interpolation in this
    spline. knot shall be the sequence of distinct knots used to define
    the spline basis functions. interpolation is fixed as
    "polynomialSpline". isPolynomial is fixed as “true”. knotType is not
    relevant for Bezier curve segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
