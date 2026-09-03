from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Minutes:
    class Meta:
        name = "minutes"
        namespace = "http://www.opengis.net/gml/3.2"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 59,
        },
    )
