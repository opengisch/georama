from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ParameterType:
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
