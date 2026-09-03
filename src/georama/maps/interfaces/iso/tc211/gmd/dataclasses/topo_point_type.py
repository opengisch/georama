from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_topo_primitive_type import (
    DirectedNode,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_topology_type import (
    AbstractTopologyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPointType(AbstractTopologyType):
    directed_node: DirectedNode | None = field(
        default=None,
        metadata={
            "name": "directedNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
