from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.decimal_minutes import DecimalMinutes
from georama.maps.interfaces.opengis.filter_1_1_0.degrees import Degrees
from georama.maps.interfaces.opengis.filter_1_1_0.minutes import Minutes
from georama.maps.interfaces.opengis.filter_1_1_0.seconds import Seconds

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DmsangleType:
    """
    Angle value provided in degree-minute-second or degree-minute format.
    """

    class Meta:
        name = "DMSAngleType"

    degrees: Optional[Degrees] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    decimal_minutes: Optional[DecimalMinutes] = field(
        default=None,
        metadata={
            "name": "decimalMinutes",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    minutes: Optional[Minutes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    seconds: Optional[Seconds] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
