from dataclasses import dataclass, field

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
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    locale: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
