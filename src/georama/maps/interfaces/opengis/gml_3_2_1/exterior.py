from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_ring_property_type import (
    AbstractRingPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Exterior(AbstractRingPropertyType):
    """A boundary of a surface consists of a number of rings.

    In the normal 2D case, one of these rings is distinguished as being
    the exterior boundary. In a general manifold this is not always
    possible, in which case all boundaries shall be listed as interior
    boundaries, and the exterior will be empty.
    """

    class Meta:
        name = "exterior"
        namespace = "http://www.opengis.net/gml/3.2"
