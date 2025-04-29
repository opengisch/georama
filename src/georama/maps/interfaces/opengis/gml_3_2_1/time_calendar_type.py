from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.time_calendar_era_property_type import (
    TimeCalendarEraPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.time_reference_system_type import (
    TimeReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCalendarType(TimeReferenceSystemType):
    reference_frame: list[TimeCalendarEraPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "referenceFrame",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
