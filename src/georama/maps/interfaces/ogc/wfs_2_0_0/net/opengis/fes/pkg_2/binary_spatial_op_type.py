from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.fes.pkg_2.function_type import Function
from wfs_2_0_0.net.opengis.fes.pkg_2.literal import Literal
from wfs_2_0_0.net.opengis.fes.pkg_2.spatial_ops_type import SpatialOpsType
from wfs_2_0_0.net.opengis.fes.pkg_2.value_reference import ValueReference

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class BinarySpatialOpType(SpatialOpsType):
    literal: list[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        },
    )
    function: list[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        },
    )
    value_reference: list[ValueReference] = field(
        default_factory=list,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "max_occurs": 2,
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 2,
        },
    )
