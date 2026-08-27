from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.distance import Distance
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.length import Length
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class LengthPropertyType:
    class Meta:
        name = "Length_PropertyType"

    distance: Distance | None = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    length: Length | None = field(
        default=None,
        metadata={
            "name": "Length",
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
