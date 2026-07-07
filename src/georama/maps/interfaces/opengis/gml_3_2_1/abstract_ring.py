from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_ring_type import (
    AbstractRingType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractRing(AbstractRingType):
    """An abstraction of a ring to support surface boundaries of different
    complexity.

    The AbstractRing element is the abstract head of the substituition
    group for all closed boundaries of a surface patch.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
