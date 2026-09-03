from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.location_property_type import (
    LocationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PriorityLocationPropertyType(LocationPropertyType):
    priority: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
