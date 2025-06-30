from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


class TemporalOperatorNameTypeValue(Enum):
    AFTER = "After"
    BEFORE = "Before"
    BEGINS = "Begins"
    BEGUN_BY = "BegunBy"
    TCONTAINS = "TContains"
    DURING = "During"
    TEQUALS = "TEquals"
    TOVERLAPS = "TOverlaps"
    MEETS = "Meets"
    OVERLAPPED_BY = "OverlappedBy"
    MET_BY = "MetBy"
    ENDS = "Ends"
    ENDED_BY = "EndedBy"
