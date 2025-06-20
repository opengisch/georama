from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.animate_color_type import (
    AnimateColorType,
)

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/Language"


@dataclass
class AnimateColor1(AnimateColorType):
    class Meta:
        name = "animateColor"
        namespace = "http://www.w3.org/2001/SMIL20/Language"
