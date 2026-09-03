from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Boolean2:
    class Meta:
        name = "Boolean"
        namespace = "http://www.isotc211.org/2005/gco"

    value: bool | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
