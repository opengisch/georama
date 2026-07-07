from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


class StateValueTypeValue(Enum):
    VALID = "valid"
    SUPERSEDED = "superseded"
    RETIRED = "retired"
    FUTURE = "future"
