from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_ring_property_type import (
    AbstractRingPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Interior(AbstractRingPropertyType):
    """A boundary of a surface consists of a number of rings.

    The "interior" rings seperate the surface / surface patch from the
    area enclosed by the rings.
    """

    class Meta:
        name = "interior"
        namespace = "http://www.opengis.net/gml"
