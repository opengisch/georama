from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.fes.pkg_2.comparison_ops_type import ComparisonOpsType
from wfs_2_0_0.net.opengis.fes.pkg_2.function_type import Function
from wfs_2_0_0.net.opengis.fes.pkg_2.literal import Literal
from wfs_2_0_0.net.opengis.fes.pkg_2.match_action_type import MatchActionType
from wfs_2_0_0.net.opengis.fes.pkg_2.value_reference import ValueReference

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class BinaryComparisonOpType(ComparisonOpsType):
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
    match_case: bool = field(
        default=True,
        metadata={
            "name": "matchCase",
            "type": "Attribute",
        },
    )
    match_action: MatchActionType = field(
        default=MatchActionType.ANY,
        metadata={
            "name": "matchAction",
            "type": "Attribute",
        },
    )
