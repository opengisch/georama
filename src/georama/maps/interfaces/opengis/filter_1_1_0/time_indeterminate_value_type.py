from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class TimeIndeterminateValueType(Enum):
    """
    This enumerated data type specifies values for indeterminate positions.
    """

    AFTER = "after"
    BEFORE = "before"
    NOW = "now"
    UNKNOWN = "unknown"
