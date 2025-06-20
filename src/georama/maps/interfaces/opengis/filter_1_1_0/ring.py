from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.ring_type import RingType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Ring(RingType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
