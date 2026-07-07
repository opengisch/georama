from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.linear_ring import LinearRing

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearRingPropertyType:
    """
    Encapsulates a ring to represent properties in features or geometry
    collections.
    """

    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
