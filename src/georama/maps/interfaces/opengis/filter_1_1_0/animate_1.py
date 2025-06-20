from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.animate_type import AnimateType

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/Language"


@dataclass
class Animate1(AnimateType):
    class Meta:
        name = "animate"
        namespace = "http://www.w3.org/2001/SMIL20/Language"
