from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class DistanceType:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
