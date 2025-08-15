from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_topology_type import (
    AbstractTopologyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Topology(AbstractTopologyType):
    class Meta:
        name = "_Topology"
        namespace = "http://www.opengis.net/gml"
