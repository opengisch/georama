from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Boolean1:
    class Meta:
        name = "Boolean"
        nillable = True
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[bool] = field(
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
