from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.binary_operator_type import (
    Add,
    Div,
    Function,
    Mul,
    Sub,
)
from georama.maps.interfaces.opengis.filter_1_1_0.comparison_ops_type import (
    ComparisonOpsType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.literal import Literal
from georama.maps.interfaces.opengis.filter_1_1_0.property_name import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class BinaryComparisonOpType(ComparisonOpsType):
    literal: list[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    function: list[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    property_name: list[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    div: list[Div] = field(
        default_factory=list,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    mul: list[Mul] = field(
        default_factory=list,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    sub: list[Sub] = field(
        default_factory=list,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    add: list[Add] = field(
        default_factory=list,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
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
