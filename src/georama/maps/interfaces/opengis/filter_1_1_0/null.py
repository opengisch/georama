from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.null_enumeration_value import (
    NullEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Null:
    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: str | NullEnumerationValue = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"other:\w{2,}",
        },
    )
