from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.linear_ring_type import LinearRingType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearRing(LinearRingType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
