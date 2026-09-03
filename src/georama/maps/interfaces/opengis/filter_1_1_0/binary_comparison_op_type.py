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
    choice: list[Literal | Function | PropertyName | Div | Mul | Sub | Add] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Literal",
                    "type": Literal,
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "Function",
                    "type": Function,
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "PropertyName",
                    "type": PropertyName,
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "Div",
                    "type": Div,
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "Mul",
                    "type": Mul,
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "Sub",
                    "type": Sub,
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "Add",
                    "type": Add,
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
            ),
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
