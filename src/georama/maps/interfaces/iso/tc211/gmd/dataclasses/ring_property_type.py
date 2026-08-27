from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ring import Ring

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RingPropertyType:
    """
    A property with the content model of gml:RingPropertyType encapsulates a ring
    to represent a component of a surface boundary.
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
