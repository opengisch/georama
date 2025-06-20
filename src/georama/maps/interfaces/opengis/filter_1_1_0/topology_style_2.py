from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topology_style_property_type import (
    TopologyStylePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopologyStyle2(TopologyStylePropertyType):
    class Meta:
        name = "topologyStyle"
        namespace = "http://www.opengis.net/gml"
