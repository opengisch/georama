from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.time_calendar_type import (
    TimeCalendarType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCalendar(TimeCalendarType):
    """A calendar is a discrete temporal reference system that provides a basis for
    defining temporal position to a resolution of one day.

    gml:TimeCalendar adds one property to those inherited from
    gml:TimeReferenceSystem. A gml:referenceFrame provides a link to a
    gml:TimeCalendarEra that it uses. A  gml:TimeCalendar may reference
    more than one calendar era. The referenceFrame element follows the
    standard GML property model, allowing the association to be
    instantiated either using an inline description using the
    gml:TimeCalendarEra element, or a link to a gml:TimeCalendarEra
    which is explicit elsewhere.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
