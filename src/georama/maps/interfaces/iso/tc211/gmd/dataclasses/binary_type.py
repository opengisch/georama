from dataclasses import dataclass, field

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
    src: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
