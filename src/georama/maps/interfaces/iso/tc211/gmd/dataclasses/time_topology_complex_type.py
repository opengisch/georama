from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_time_complex_type import (
    AbstractTimeComplexType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_topology_primitive_property_type import (
    TimeTopologyPrimitivePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeTopologyComplexType(AbstractTimeComplexType):
    primitive: list[TimeTopologyPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
