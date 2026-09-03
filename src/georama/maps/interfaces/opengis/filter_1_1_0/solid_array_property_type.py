from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.composite_solid_type import (
    CompositeSolid,
)
from georama.maps.interfaces.opengis.filter_1_1_0.solid import Solid

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidArrayPropertyType:
    """A container for an array of solids.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """

    solid_or_composite_solid: list[Solid | CompositeSolid] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Solid",
                    "type": Solid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSolid",
                    "type": CompositeSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
