from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.solid import Solid
from georama.maps.interfaces.opengis.gml_3_2_1.solid_property_type import CompositeSolid

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SolidArrayPropertyType:
    """Gml:SolidArrayPropertyType is a container for an array of solids.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """

    composite_solid: list[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    solid: list[Solid] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
