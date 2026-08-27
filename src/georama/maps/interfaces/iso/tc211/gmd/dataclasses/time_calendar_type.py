from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_calendar_era_property_type import (
    TimeCalendarEraPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_reference_system_type import (
    TimeReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCalendarType(TimeReferenceSystemType):
    reference_frame: list[TimeCalendarEraPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "referenceFrame",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
