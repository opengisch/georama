from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.unlimited_integer import UnlimitedInteger

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class UnlimitedIntegerPropertyType:
    class Meta:
        name = "UnlimitedInteger_PropertyType"

    unlimited_integer: UnlimitedInteger | None = field(
        default=None,
        metadata={
            "name": "UnlimitedInteger",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "nillable": True,
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
