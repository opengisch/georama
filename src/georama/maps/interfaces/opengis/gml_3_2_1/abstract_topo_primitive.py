from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_topo_primitive_type import (
    AbstractTopoPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTopoPrimitive(AbstractTopoPrimitiveType):
    """Gml:AbstractTopoPrimitive acts as the base type for all topological
    primitives.

    Topology primitives are the atomic (smallest possible) units of a
    topology complex. Each topology primitive may contain references to
    other topology primitives of codimension 2 or more (gml:isolated).
    Conversely, nodes may have faces as containers and nodes and edges
    may have solids as containers (gml:container).
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
