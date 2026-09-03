from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class DistanceType:
    value: float | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    units: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
