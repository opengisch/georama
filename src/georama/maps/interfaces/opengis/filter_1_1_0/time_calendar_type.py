from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_reference_system_type import (
    AbstractTimeReferenceSystemType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.time_calendar_era_property_type import (
    TimeCalendarEraPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCalendarType(AbstractTimeReferenceSystemType):
    """A calendar is a discrete temporal reference system that provides a basis for
    defining temporal position to a resolution of one day.

    A single calendar may reference more than one calendar era.

    :ivar reference_frame: Link to the CalendarEras that it uses as a
        reference for dating.
    """

    reference_frame: list[TimeCalendarEraPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "referenceFrame",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
