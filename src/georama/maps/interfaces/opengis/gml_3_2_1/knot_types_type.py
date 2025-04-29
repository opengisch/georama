from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class KnotTypesType(Enum):
    """
    This enumeration type specifies values for the knots' type (see ISO 19107:2003,
    6.4.25).
    """

    UNIFORM = "uniform"
    QUASI_UNIFORM = "quasiUniform"
    PIECEWISE_BEZIER = "piecewiseBezier"
