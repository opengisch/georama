from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.scoped_name import ScopedName

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class ScopedNamePropertyType:
    class Meta:
        name = "ScopedName_PropertyType"

    scoped_name: ScopedName | None = field(
        default=None,
        metadata={
            "name": "ScopedName",
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
