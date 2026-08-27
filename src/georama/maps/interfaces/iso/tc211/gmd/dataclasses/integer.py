from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Integer:
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
