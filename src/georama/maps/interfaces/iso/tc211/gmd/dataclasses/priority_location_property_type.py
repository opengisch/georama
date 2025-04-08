from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.location_property_type import (
    LocationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PriorityLocationPropertyType(LocationPropertyType):
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
