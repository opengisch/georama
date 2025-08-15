from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.topo_primitive_member_type import (
    TopoPrimitiveMemberType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoPrimitiveMember(TopoPrimitiveMemberType):
    """
    The gml:topoPrimitiveMember property element encodes for the relationship
    between a topology complex and a single topology primitive.
    """

    class Meta:
        name = "topoPrimitiveMember"
        namespace = "http://www.opengis.net/gml/3.2"
