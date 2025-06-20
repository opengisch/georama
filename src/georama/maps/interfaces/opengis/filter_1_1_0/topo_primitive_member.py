from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topo_primitive_member_type import (
    TopoPrimitiveMemberType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitiveMember(TopoPrimitiveMemberType):
    class Meta:
        name = "topoPrimitiveMember"
        namespace = "http://www.opengis.net/gml"
