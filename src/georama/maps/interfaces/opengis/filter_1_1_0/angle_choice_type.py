from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.angle import Angle
from georama.maps.interfaces.opengis.filter_1_1_0.dms_angle import DmsAngle

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AngleChoiceType:
    """
    Value of an angle quantity provided in either degree-minute-second format or
    single value format.
    """

    angle: Optional[Angle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dms_angle: Optional[DmsAngle] = field(
        default=None,
        metadata={
            "name": "dmsAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
