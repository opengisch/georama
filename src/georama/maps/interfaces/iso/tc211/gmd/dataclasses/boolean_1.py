from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Boolean1:
    class Meta:
        name = "Boolean"
        nillable = True
        namespace = "http://www.opengis.net/gml"

    value: bool | None = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
