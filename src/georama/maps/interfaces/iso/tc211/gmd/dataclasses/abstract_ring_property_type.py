from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.linear_ring import LinearRing
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ring import Ring

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractRingPropertyType:
    """
    A property with the content model of gml:AbstractRingPropertyType encapsulates
    a ring to represent the surface boundary property of a surface.
    """

    ring: Ring | None = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_ring: LinearRing | None = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
