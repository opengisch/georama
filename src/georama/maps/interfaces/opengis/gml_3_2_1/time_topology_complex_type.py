from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_complex_type import (
    AbstractTimeComplexType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.time_topology_primitive_property_type import (
    TimeTopologyPrimitivePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeTopologyComplexType(AbstractTimeComplexType):
    primitive: list[TimeTopologyPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
