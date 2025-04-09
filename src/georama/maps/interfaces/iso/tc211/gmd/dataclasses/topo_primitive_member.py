from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.topo_primitive_member_type import (
    TopoPrimitiveMemberType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitiveMember(TopoPrimitiveMemberType):
    """
    The gml:topoPrimitiveMember property element encodes for the relationship
    between a topology complex and a single topology primitive.
    """

    class Meta:
        name = "topoPrimitiveMember"
        namespace = "http://www.opengis.net/gml"
