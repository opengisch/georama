from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_topology_type import (
    AbstractTopologyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTopology(AbstractTopologyType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
