from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.angle_choice_type import (
    AngleChoiceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GreenwichLongitude(AngleChoiceType):
    """Longitude of the prime meridian measured from the Greenwich meridian,
    positive eastward.

    The greenwichLongitude most common value is zero, and that value
    shall be used when the meridianName value is Greenwich.
    """

    class Meta:
        name = "greenwichLongitude"
        namespace = "http://www.opengis.net/gml"
