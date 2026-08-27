from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_topology_type import (
    AbstractTopologyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.face_or_topo_solid_property_type import (
    DirectedNode,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoPointType(AbstractTopologyType):
    directed_node: DirectedNode | None = field(
        default=None,
        metadata={
            "name": "directedNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
