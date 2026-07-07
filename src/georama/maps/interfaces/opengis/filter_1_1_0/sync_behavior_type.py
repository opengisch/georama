from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


class SyncBehaviorType(Enum):
    CAN_SLIP = "canSlip"
    LOCKED = "locked"
    INDEPENDENT = "independent"
    DEFAULT = "default"
