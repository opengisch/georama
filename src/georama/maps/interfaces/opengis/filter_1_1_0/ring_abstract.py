from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_ring_type import (
    AbstractRingType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RingAbstract(AbstractRingType):
    """
    The "_Ring" element is the abstract head of the substituition group for all
    closed boundaries of a surface patch.
    """

    class Meta:
        name = "_Ring"
        namespace = "http://www.opengis.net/gml"
