from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.linear_ring import LinearRing
from georama.maps.interfaces.opengis.filter_1_1_0.ring import Ring

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractRingPropertyType:
    """
    Encapsulates a ring to represent the surface boundary property of a surface.
    """

    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
