from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class LineTypeType(Enum):
    """
    Graph-specific styling property.
    """

    STRAIGHT = "STRAIGHT"
    BENT = "BENT"
