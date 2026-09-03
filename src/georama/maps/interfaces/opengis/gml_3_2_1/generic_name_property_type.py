from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.local_name import LocalName
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.scoped_name import ScopedName

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class GenericNamePropertyType:
    class Meta:
        name = "GenericName_PropertyType"

    scoped_name: ScopedName | None = field(
        default=None,
        metadata={
            "name": "ScopedName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    local_name: LocalName | None = field(
        default=None,
        metadata={
            "name": "LocalName",
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
