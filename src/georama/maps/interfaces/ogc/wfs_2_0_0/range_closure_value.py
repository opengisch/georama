from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


class RangeClosureValue(Enum):
    """
    :cvar CLOSED: The specified minimum and maximum values are included
        in this range.
    :cvar OPEN: The specified minimum and maximum values are NOT
        included in this range.
    :cvar OPEN_CLOSED: The specified minimum value is NOT included in
        this range, and the specified maximum value IS included in this
        range.
    :cvar CLOSED_OPEN: The specified minimum value IS included in this
        range, and the specified maximum value is NOT included in this
        range.
    """

    CLOSED = "closed"
    OPEN = "open"
    OPEN_CLOSED = "open-closed"
    CLOSED_OPEN = "closed-open"
