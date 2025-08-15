from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


class VersionActionTokens(Enum):
    FIRST = "FIRST"
    LAST = "LAST"
    PREVIOUS = "PREVIOUS"
    NEXT = "NEXT"
    ALL = "ALL"
