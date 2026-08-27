from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.decimal_minutes import DecimalMinutes
from georama.maps.interfaces.opengis.gml_3_2_1.degrees import Degrees
from georama.maps.interfaces.opengis.gml_3_2_1.minutes import Minutes
from georama.maps.interfaces.opengis.gml_3_2_1.seconds import Seconds

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DmsangleType:
    class Meta:
        name = "DMSAngleType"

    degrees: Degrees | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    decimal_minutes: DecimalMinutes | None = field(
        default=None,
        metadata={
            "name": "decimalMinutes",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    minutes: Minutes | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    seconds: Seconds | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
