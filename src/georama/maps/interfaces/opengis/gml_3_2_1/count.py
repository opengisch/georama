from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Count:
    class Meta:
        nillable = True
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
