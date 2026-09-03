from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CountExtent:
    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: list[str | NilReasonEnumerationValue] = field(
        default_factory=list,
        metadata={
            "length": 2,
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
