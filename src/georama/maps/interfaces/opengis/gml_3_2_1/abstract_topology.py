from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_topology_type import (
    AbstractTopologyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTopology(AbstractTopologyType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
