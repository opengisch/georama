from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_primitive_type import (
    TimePeriodPropertyType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType
from georama.maps.interfaces.opengis.filter_1_1_0.string_or_ref_type import (
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCalendarEraType(DefinitionType):
    """In every calendar, years are numbered relative to the date of a reference
    event that defines a calendar era.

    In this implementation, we omit the back-pointer "datingSystem".

    :ivar reference_event: Name or description of a mythical or historic
        event which fixes the position of the base scale of the calendar
        era.
    :ivar reference_date: Date of the referenceEvent expressed as a date
        in the given calendar. In most calendars, this date is the
        origin (i.e., the first day) of the scale, but this is not
        always true.
    :ivar julian_reference: Julian date that corresponds to the
        reference date. The Julian day numbering system is a temporal
        coordinate system that has an origin earlier than any known
        calendar, at noon on 1 January 4713 BC in the Julian proleptic
        calendar. The Julian day number is an integer value; the Julian
        date is a decimal value that allows greater resolution.
        Transforming calendar dates to and from Julian dates provides a
        relatively simple basis for transforming dates from one calendar
        to another.
    :ivar epoch_of_use: Period for which the calendar era was used as a
        basis for dating.
    """

    reference_event: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    reference_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "referenceDate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    julian_reference: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "julianReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    epoch_of_use: Optional[TimePeriodPropertyType] = field(
        default=None,
        metadata={
            "name": "epochOfUse",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
