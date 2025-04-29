from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.time_topology_complex_type import (
    TimeTopologyComplexType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeTopologyComplex(TimeTopologyComplexType):
    """A temporal topology complex shall be the connected acyclic directed graph
    composed of temporal topological primitives, i.e. time nodes and time edges.

    Because a time edge may not exist without two time nodes on its
    boundaries, static features have time edges from a temporal topology
    complex as the values of their temporal properties, regardless of
    explicit declarations. A temporal topology complex expresses a
    linear or a non-linear graph. A temporal linear graph, composed of a
    sequence of time edges, provides a lineage described only by
    "substitution" of feature instances or feature element values. A
    time node as the start or the end of the graph connects with at
    least one time edge. A time node other than the start and the end
    shall connect to at least two time edges: one of starting from the
    node, and another ending at the node. A temporal topological complex
    is a set of connected temporal topological primitives. The member
    primtives are indicated, either by reference or by value, using the
    primitive property.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
