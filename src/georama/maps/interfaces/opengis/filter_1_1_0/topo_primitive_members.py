from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topo_primitive_array_association_type import (
    TopoPrimitiveArrayAssociationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitiveMembers(TopoPrimitiveArrayAssociationType):
    class Meta:
        name = "topoPrimitiveMembers"
        namespace = "http://www.opengis.net/gml"
