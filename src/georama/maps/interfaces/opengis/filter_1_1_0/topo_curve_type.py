from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_topo_primitive_type import (
    DirectedEdge,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_topology_type import (
    AbstractTopologyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoCurveType(AbstractTopologyType):
    """The end Node of each directedEdge of a TopoCurveType is the start Node of
    the next directedEdge of the TopoCurveType in document order.

    The TopoCurve type and element represent a homogeneous topological
    expression, a list of directed edges, which if realised are
    isomorphic to a geometric curve primitive. The intended use of
    TopoCurve is to appear within a line feature instance to express the
    structural and geometric relationships of this line to other
    features via the shared edge definitions.
    """

    directed_edge: list[DirectedEdge] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
