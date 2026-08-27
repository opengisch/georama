from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.scale import Scale

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class ScalePropertyType:
    class Meta:
        name = "Scale_PropertyType"

    scale: Scale | None = field(
        default=None,
        metadata={
            "name": "Scale",
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
