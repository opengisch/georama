from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_reference_system_type import (
    AbstractTimeReferenceSystemType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.string_or_ref_type import (
    StringOrRefType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.time_calendar_property_type import (
    TimeCalendarPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeClockType(AbstractTimeReferenceSystemType):
    """A clock provides a basis for defining temporal position within a day.

    A clock must be used with a calendar in order to provide a complete
    description of a temporal position within a specific day.

    :ivar reference_event: Name or description of an event, such as
        solar noon or sunrise, which fixes the position of the base
        scale of the clock.
    :ivar reference_time: time of day associated with the reference
        event expressed as a time of day in the given clock. The
        reference time is usually the origin of the clock scale.
    :ivar utc_reference: 24 hour local or UTC time that corresponds to
        the reference time.
    :ivar date_basis:
    """

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
