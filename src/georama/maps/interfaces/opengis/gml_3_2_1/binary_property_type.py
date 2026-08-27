from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.binary import Binary
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class BinaryPropertyType:
    class Meta:
        name = "Binary_PropertyType"

    binary: Binary | None = field(
        default=None,
        metadata={
            "name": "Binary",
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
