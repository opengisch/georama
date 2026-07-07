from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.point import Point

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointArrayPropertyType:
    """Gml:PointArrayPropertyType is a container for an array of points.

    The elements are always contained inline in the array property,
    referencing geometry elements or arrays of geometry elements via
    XLinks is not supported.
    """

    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
