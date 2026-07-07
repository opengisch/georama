from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.time_calendar_era_type import (
    TimeCalendarEraType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCalendarEra(TimeCalendarEraType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
