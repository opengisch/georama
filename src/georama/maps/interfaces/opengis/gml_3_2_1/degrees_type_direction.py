from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class DegreesTypeDirection(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"
    PLUS_SIGN = "+"
    HYPHEN_MINUS = "-"
