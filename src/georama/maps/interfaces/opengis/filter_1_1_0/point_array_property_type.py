from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.point import Point

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointArrayPropertyType:
    """A container for an array of points.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """

    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
