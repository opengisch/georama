from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_topo_primitive_type import (
    Edge,
    Face,
    Node,
    TopoSolid,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitiveArrayAssociationType:
    topo_solid: list[TopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    face: list[Face] = field(
        default_factory=list,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    edge: list[Edge] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    node: list[Node] = field(
        default_factory=list,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
