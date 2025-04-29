from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class Url:
    class Meta:
        name = "URL"
        namespace = "http://www.isotc211.org/2005/gmd"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
