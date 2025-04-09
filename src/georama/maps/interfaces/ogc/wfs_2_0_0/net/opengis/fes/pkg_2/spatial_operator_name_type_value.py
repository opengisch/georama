from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


class SpatialOperatorNameTypeValue(Enum):
    BBOX = "BBOX"
    EQUALS = "Equals"
    DISJOINT = "Disjoint"
    INTERSECTS = "Intersects"
    TOUCHES = "Touches"
    CROSSES = "Crosses"
    WITHIN = "Within"
    CONTAINS = "Contains"
    OVERLAPS = "Overlaps"
    BEYOND = "Beyond"
    DWITHIN = "DWithin"
