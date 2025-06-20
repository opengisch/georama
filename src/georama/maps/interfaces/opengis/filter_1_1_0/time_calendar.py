from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.time_calendar_type import (
    TimeCalendarType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCalendar(TimeCalendarType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
