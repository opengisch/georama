from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.horizontal_angle import (
    HorizontalAngle,
)
from georama.maps.interfaces.opengis.filter_1_1_0.vector import Vector
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_angle import VerticalAngle

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DirectionVectorType:
    """
    Direction expressed as a vector, either using components, or using angles.
    """

    vector_or_horizontal_angle_or_vertical_angle: list[
        Vector | HorizontalAngle | VerticalAngle
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "vector",
                    "type": Vector,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "horizontalAngle",
                    "type": HorizontalAngle,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "verticalAngle",
                    "type": VerticalAngle,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
            "max_occurs": 2,
        },
    )
