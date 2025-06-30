from dataclasses import dataclass, field
from typing import Union

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_topo_primitive_type import (
    Edge,
    Face,
    Node,
    TopoSolid,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitiveArrayAssociationType:
    """
    This type supports embedding an array of topological primitives in a
    TopoComplex.
    """

    choice: list[Union[TopoSolid, Face, Edge, Node]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TopoSolid",
                    "type": TopoSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Face",
                    "type": Face,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Edge",
                    "type": Edge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Node",
                    "type": Node,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
