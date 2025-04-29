from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.degrees_type_direction import (
    DegreesTypeDirection,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DegreesType:
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 359,
        },
    )
    direction: Optional[DegreesTypeDirection] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
