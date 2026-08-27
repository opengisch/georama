from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.angle_type import AngleType
from georama.maps.interfaces.opengis.gml_3_2_1.vector import Vector

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectionVectorType:
    """
    Direction vectors are specified by providing components of a vector.
    """

    vector: Vector | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    horizontal_angle: AngleType | None = field(
        default=None,
        metadata={
            "name": "horizontalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_angle: AngleType | None = field(
        default=None,
        metadata={
            "name": "verticalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
