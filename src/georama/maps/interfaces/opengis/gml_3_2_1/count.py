from dataclasses import dataclass, field
from typing import Optional

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
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
        },
    )
