from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.boolean_2 import Boolean2
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class BooleanPropertyType2:
    class Meta:
        name = "Boolean_PropertyType"

    boolean: Boolean2 | None = field(
        default=None,
        metadata={
            "name": "Boolean",
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
