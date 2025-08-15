from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_complex_type import (
    AbstractTimeComplexType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.time_topology_primitive_property_type import (
    TimeTopologyPrimitivePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeTopologyComplexType(AbstractTimeComplexType):
    """
    A temporal topology complex.
    """

    primitive: list[TimeTopologyPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
