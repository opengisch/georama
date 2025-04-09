from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_topo_primitive_type import (
    DirectedFace,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_topology_type import (
    AbstractTopologyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.aggregation_type import (
    AggregationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoSurfaceType(AbstractTopologyType):
    directed_face: List[DirectedFace] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
