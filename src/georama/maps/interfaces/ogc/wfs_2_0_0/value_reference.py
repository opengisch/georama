from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ValueReference:
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
