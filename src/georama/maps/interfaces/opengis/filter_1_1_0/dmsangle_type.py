from dataclasses import dataclass, field
from typing import Optional, Union

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
    decimal_minutes_or_minutes_or_seconds: list[Union[DecimalMinutes, Minutes, Seconds]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "decimalMinutes",
                        "type": DecimalMinutes,
                        "namespace": "http://www.opengis.net/gml",
                    },
                    {
                        "name": "minutes",
                        "type": Minutes,
                        "namespace": "http://www.opengis.net/gml",
                    },
                    {
                        "name": "seconds",
                        "type": Seconds,
                        "namespace": "http://www.opengis.net/gml",
                    },
                ),
                "max_occurs": 2,
            },
        )
    )
