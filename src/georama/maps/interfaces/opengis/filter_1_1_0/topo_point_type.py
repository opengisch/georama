from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_topo_primitive_type import (
    DirectedNode,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_topology_type import (
    AbstractTopologyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPointType(AbstractTopologyType):
    """The intended use of TopoPoint is to appear within a point feature to express
    the structural and possibly geometric relationships of this point to other
    features via shared node definitions.

    Note the orientation assigned to the directedNode has no meaning in
    this context. It is preserved for symmetry with the types and
    elements which follow.
    """

    directed_node: Optional[DirectedNode] = field(
        default=None,
        metadata={
            "name": "directedNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
