from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate, XmlPeriod

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_time_primitive_type import (
    TimePeriodPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_type import (
    DefinitionType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.string_or_ref_type import (
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCalendarEraType(DefinitionType):
    reference_event: StringOrRefType | None = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    reference_date: XmlDate | XmlPeriod | None = field(
        default=None,
        metadata={
            "name": "referenceDate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    julian_reference: Decimal | None = field(
        default=None,
        metadata={
            "name": "julianReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    epoch_of_use: TimePeriodPropertyType | None = field(
        default=None,
        metadata={
            "name": "epochOfUse",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
