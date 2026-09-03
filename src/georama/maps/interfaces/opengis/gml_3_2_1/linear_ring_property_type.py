from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.linear_ring import LinearRing

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearRingPropertyType:
    """
    A property with the content model of gml:LinearRingPropertyType encapsulates a
    linear ring to represent a component of a surface boundary.
    """

    linear_ring: LinearRing | None = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
