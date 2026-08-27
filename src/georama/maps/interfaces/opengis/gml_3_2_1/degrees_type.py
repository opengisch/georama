from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.degrees_type_direction import (
    DegreesTypeDirection,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DegreesType:
    value: int | None = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 359,
        },
    )
    direction: DegreesTypeDirection | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
