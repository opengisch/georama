from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.compass_point_enumeration import (
    CompassPointEnumeration,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CompassPoint:
    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: Optional[CompassPointEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
