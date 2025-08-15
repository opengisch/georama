from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.time_interval_length_type import (
    TimeIntervalLengthType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeInterval(TimeIntervalLengthType):
    """
    This element is a valid subtype of TimeDurationType according to section
    3.14.6, rule 2.2.4 in XML Schema, Part 1.
    """

    class Meta:
        name = "timeInterval"
        namespace = "http://www.opengis.net/gml"
