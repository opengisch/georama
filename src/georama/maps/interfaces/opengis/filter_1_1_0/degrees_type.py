from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.degrees_type_value import (
    DegreesTypeValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DegreesType:
    """Integer number of degrees, plus the angle direction.

    This element can be used for geographic Latitude and Longitude. For
    Latitude, the XML attribute direction can take the values "N" or
    "S", meaning North or South of the equator. For Longitude, direction
    can take the values "E" or "W", meaning East or West of the prime
    meridian. This element can also be used for other angles. In that
    case, the direction can take the values "+" or "-" (of SignType), in
    the specified rotational direction from a specified reference
    direction.
    """

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 359,
        },
    )
    direction: DegreesTypeValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
