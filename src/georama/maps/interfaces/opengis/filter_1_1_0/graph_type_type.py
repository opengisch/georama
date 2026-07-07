from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class GraphTypeType(Enum):
    """
    Graph-specific styling property.
    """

    TREE = "TREE"
    BICONNECTED = "BICONNECTED"
