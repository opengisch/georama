from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.ring import Ring

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RingPropertyType:
    """
    Encapsulates a ring to represent properties in features or geometry
    collections.
    """

    ring: Ring | None = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
