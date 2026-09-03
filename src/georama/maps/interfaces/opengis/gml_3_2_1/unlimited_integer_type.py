from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class UnlimitedIntegerType:
    class Meta:
        name = "UnlimitedInteger_Type"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    is_infinite: bool | None = field(
        default=None,
        metadata={
            "name": "isInfinite",
            "type": "Attribute",
        },
    )
