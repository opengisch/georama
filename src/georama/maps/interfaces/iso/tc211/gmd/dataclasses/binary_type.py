from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class BinaryType:
    class Meta:
        name = "Binary_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
