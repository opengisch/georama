from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


class TimeUnitTypeValue(Enum):
    YEAR = "year"
    MONTH = "month"
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    SECOND = "second"
