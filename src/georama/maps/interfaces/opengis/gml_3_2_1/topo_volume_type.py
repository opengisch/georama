from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_topology_type import (
    AbstractTopologyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType
from georama.maps.interfaces.opengis.gml_3_2_1.face_or_topo_solid_property_type import (
    DirectedTopoSolid,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoVolumeType(AbstractTopologyType):
    directed_topo_solid: list[DirectedTopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "directedTopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    aggregation_type: AggregationType | None = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
