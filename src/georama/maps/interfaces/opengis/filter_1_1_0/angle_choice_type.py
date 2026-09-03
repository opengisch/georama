from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.angle import Angle
from georama.maps.interfaces.opengis.filter_1_1_0.dms_angle import DmsAngle

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AngleChoiceType:
    """
    Value of an angle quantity provided in either degree-minute-second format or
    single value format.
    """

    angle_or_dms_angle: Angle | DmsAngle | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "angle",
                    "type": Angle,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "dmsAngle",
                    "type": DmsAngle,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
