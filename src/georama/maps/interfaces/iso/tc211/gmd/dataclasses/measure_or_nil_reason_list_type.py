from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MeasureOrNilReasonListType:
    """Gml:MeasureOrNilReasonListType provides for a list of quantities.

    An instance element may also include embedded values from
    NilReasonType. It is intended to be used in situations where a value
    is expected, but the value may be absent for some reason.
    """

    value: list[str | NilReasonEnumerationValue] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
    uom: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        },
    )
