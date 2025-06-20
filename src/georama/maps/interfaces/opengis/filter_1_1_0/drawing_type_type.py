from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class DrawingTypeType(Enum):
    """
    Graph-specific styling property.
    """

    POLYLINE = "POLYLINE"
    ORTHOGONAL = "ORTHOGONAL"
