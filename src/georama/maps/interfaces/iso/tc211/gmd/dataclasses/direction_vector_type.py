from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.angle_type import AngleType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vector import Vector

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DirectionVectorType:
    """
    Direction vectors are specified by providing components of a vector.
    """

    vector: Vector | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    horizontal_angle: AngleType | None = field(
        default=None,
        metadata={
            "name": "horizontalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_angle: AngleType | None = field(
        default=None,
        metadata={
            "name": "verticalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
