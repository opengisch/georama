from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_topo_primitive_type import (
    AbstractTopoPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitive(AbstractTopoPrimitiveType):
    """
    Substitution group branch for Topo Primitives, used by
    TopoPrimitiveArrayAssociationType.
    """

    class Meta:
        name = "_TopoPrimitive"
        namespace = "http://www.opengis.net/gml"
