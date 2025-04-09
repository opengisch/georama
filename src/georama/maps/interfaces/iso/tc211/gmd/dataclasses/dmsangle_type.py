from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.decimal_minutes import (
    DecimalMinutes,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.degrees import Degrees
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.minutes import Minutes
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.seconds import Seconds

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DmsangleType:
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
