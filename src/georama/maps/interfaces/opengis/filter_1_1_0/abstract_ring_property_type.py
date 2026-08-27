from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.linear_ring import LinearRing
from georama.maps.interfaces.opengis.filter_1_1_0.ring import Ring

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractRingPropertyType:
    """
    Encapsulates a ring to represent the surface boundary property of a surface.
    """

    ring_or_linear_ring: Ring | LinearRing | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Ring",
                    "type": Ring,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearRing",
                    "type": LinearRing,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
