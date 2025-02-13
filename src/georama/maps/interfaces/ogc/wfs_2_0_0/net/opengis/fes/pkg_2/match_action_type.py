from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


class MatchActionType(Enum):
    ALL = "All"
    ANY = "Any"
    ONE = "One"
