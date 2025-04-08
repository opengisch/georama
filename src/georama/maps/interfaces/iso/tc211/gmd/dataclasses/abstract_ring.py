from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_ring_type import (
    AbstractRingType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractRing(AbstractRingType):
    """An abstraction of a ring to support surface boundaries of different
    complexity.

    The AbstractRing element is the abstract head of the substituition
    group for all closed boundaries of a surface patch.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
