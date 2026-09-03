from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.date_time import DateTime
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class DateTimePropertyType:
    class Meta:
        name = "DateTime_PropertyType"

    date_time: DateTime | None = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
