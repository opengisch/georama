from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.time_clock_type import TimeClockType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeClock(TimeClockType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
