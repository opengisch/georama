from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class SignType(Enum):
    """Utility type used in various places
    - e.g. to indicate the direction of topological objects;
    "+" for forwards, or "-" for backwards."""

    HYPHEN_MINUS = "-"
    PLUS_SIGN = "+"
