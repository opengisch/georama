from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FunctionNameType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    n_args: str | None = field(
        default=None,
        metadata={
            "name": "nArgs",
            "type": "Attribute",
            "required": True,
        },
    )
