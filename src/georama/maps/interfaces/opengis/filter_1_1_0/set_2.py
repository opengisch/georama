from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.set_type import SetType

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


@dataclass
class Set2(SetType):
    class Meta:
        name = "set"
        namespace = "http://www.w3.org/2001/SMIL20/"
