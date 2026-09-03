from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.string_or_ref_type import (
    StringOrRefType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_calendar_property_type import (
    TimeCalendarPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_reference_system_type import (
    TimeReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeClockType(TimeReferenceSystemType):
    reference_event: StringOrRefType | None = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    reference_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "referenceTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    utc_reference: XmlTime | None = field(
        default=None,
        metadata={
            "name": "utcReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    date_basis: list[TimeCalendarPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "dateBasis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
