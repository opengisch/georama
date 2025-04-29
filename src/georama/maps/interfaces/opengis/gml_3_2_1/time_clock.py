from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.time_clock_type import TimeClockType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeClock(TimeClockType):
    """A clock provides a basis for defining temporal position within a day. A
    clock shall be used with a calendar in order to provide a complete description
    of a temporal position within a specific day.

    gml:TimeClock adds the following properties to those inherited from gml:TimeReferenceSystemType:
    -       gml:referenceEvent is the name or description of an event, such as solar noon or sunrise, which fixes the position of the base scale of the clock.
    -       gml:referenceTime specifies the time of day associated with the reference event expressed as a time of day in the given clock. The reference time is usually the origin of the clock scale.
    -       gml:utcReference specifies the 24 hour local or UTC time that corresponds to the reference time.
    -       gml:dateBasis contains or references the calendars that use this clock.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
