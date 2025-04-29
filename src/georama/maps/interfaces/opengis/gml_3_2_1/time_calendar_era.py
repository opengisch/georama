from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.time_calendar_era_type import (
    TimeCalendarEraType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCalendarEra(TimeCalendarEraType):
    """Gml:TimeCalendarEra inherits basic properties from gml:DefinitionType and
    has the following additional properties:

    -       gml:referenceEvent is the name or description of a mythical or historic event which fixes the position of the base scale of the calendar era.  This is given as text or using a link to description held elsewhere.
    -       gml:referenceDate specifies the date of the referenceEvent expressed as a date in the given calendar.  In most calendars, this date is the origin (i.e., the first day) of the scale, but this is not always true.
    -       gml:julianReference specifies the Julian date that corresponds to the reference date.  The Julian day number is an integer value; the Julian date is a decimal value that allows greater resolution.  Transforming calendar dates to and from Julian dates provides a relatively simple basis for transforming dates from one calendar to another.
    -       gml:epochOfUse is the period for which the calendar era was used as a basis for dating.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
