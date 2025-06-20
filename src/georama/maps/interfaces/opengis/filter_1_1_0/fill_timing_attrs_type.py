from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


class FillTimingAttrsType(Enum):
    REMOVE = "remove"
    FREEZE = "freeze"
    HOLD = "hold"
    AUTO = "auto"
    DEFAULT = "default"
    TRANSITION = "transition"
