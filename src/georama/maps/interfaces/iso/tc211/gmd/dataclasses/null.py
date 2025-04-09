from dataclasses import dataclass, field
from typing import Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Null:
    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: Union[str, NilReasonEnumerationValue] = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"other:\w{2,}",
        },
    )
