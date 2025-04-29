from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class TimeIndeterminateValueType(Enum):
    """These values are interpreted as follows:
    -	"unknown" indicates that no specific value for temporal position is provided.
    -	"now" indicates that the specified value shall be replaced with the current temporal position whenever the value is accessed.
    -	"before" indicates that the actual temporal position is unknown, but it is known to be before the specified value.
    -	"after" indicates that the actual temporal position is unknown, but it is known to be after the specified value.
    A value for indeterminatePosition may
    -	be used either alone, or
    -	qualify a specific value for temporal position."""

    AFTER = "after"
    BEFORE = "before"
    NOW = "now"
    UNKNOWN = "unknown"
