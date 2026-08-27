from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.curve_property_type import Ring
from georama.maps.interfaces.opengis.gml_3_2_1.linear_ring import LinearRing

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    linear_ring: LinearRing | None = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
