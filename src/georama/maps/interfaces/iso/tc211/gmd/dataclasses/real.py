from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Real:
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"

    value: float | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
