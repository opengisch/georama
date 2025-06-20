from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class KnotTypesType(Enum):
    """Defines allowed values for the knots` type.

    Uniform knots implies that all knots are of multiplicity 1 and they
    differ by a positive constant from the preceding knot. Knots are
    quasi-uniform iff they are of multiplicity (degree + 1) at the ends,
    of multiplicity 1 elsewhere, and they differ by a positive constant
    from the preceding knot.
    """

    UNIFORM = "uniform"
    QUASI_UNIFORM = "quasiUniform"
    PIECEWISE_BEZIER = "piecewiseBezier"
