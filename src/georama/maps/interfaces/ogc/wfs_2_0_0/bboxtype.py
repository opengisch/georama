from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.function_type import Function
from georama.maps.interfaces.ogc.wfs_2_0_0.literal import Literal
from georama.maps.interfaces.ogc.wfs_2_0_0.spatial_ops_type import SpatialOpsType
from georama.maps.interfaces.ogc.wfs_2_0_0.value_reference import ValueReference

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Bboxtype(SpatialOpsType):
    class Meta:
        name = "BBOXType"

    choice: list[Literal | Function | ValueReference | object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Literal",
                    "type": Literal,
                    "namespace": "http://www.opengis.net/fes/2.0",
                    "max_occurs": 2,
                },
                {
                    "name": "Function",
                    "type": Function,
                    "namespace": "http://www.opengis.net/fes/2.0",
                    "max_occurs": 2,
                },
                {
                    "name": "ValueReference",
                    "type": ValueReference,
                    "namespace": "http://www.opengis.net/fes/2.0",
                    "max_occurs": 2,
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##other",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
