from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topology_style_type import (
    TopologyStyleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopologyStyle1(TopologyStyleType):
    """The style descriptor for topologies of a feature.

    Describes individual topology elements styles.
    """

    class Meta:
        name = "TopologyStyle"
        namespace = "http://www.opengis.net/gml"
