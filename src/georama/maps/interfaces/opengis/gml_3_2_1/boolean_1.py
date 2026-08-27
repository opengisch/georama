from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Boolean1:
    class Meta:
        name = "Boolean"
        nillable = True
        namespace = "http://www.opengis.net/gml/3.2"

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
