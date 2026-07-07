from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LocalisedCharacterStringType:
    class Meta:
        name = "LocalisedCharacterString_Type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    locale: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
