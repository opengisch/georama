from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class SignType(Enum):
    """
    Gml:SignType is a convenience type with values “+” (plus) and “-“ (minus).
    """

    HYPHEN_MINUS = "-"
    PLUS_SIGN = "+"
