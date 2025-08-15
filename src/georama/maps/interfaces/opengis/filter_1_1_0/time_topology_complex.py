from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.time_topology_complex_type import (
    TimeTopologyComplexType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeTopologyComplex(TimeTopologyComplexType):
    """This element represents temporal topology complex.

    It shall be the connected acyclic directed graph composed of time
    nodes and time edges.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
