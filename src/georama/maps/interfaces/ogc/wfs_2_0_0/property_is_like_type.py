from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.ogc.wfs_2_0_0.comparison_ops_type import ComparisonOpsType
from georama.maps.interfaces.ogc.wfs_2_0_0.function_type import Function
from georama.maps.interfaces.ogc.wfs_2_0_0.literal import Literal
from georama.maps.interfaces.ogc.wfs_2_0_0.value_reference import ValueReference

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsLikeType(ComparisonOpsType):
    literal_or_function_or_value_reference: list[Union[Literal, Function, ValueReference]] = (
        field(
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
                ),
                "max_occurs": 2,
            },
        )
    )
    wild_card: Optional[str] = field(
        default=None,
        metadata={
            "name": "wildCard",
            "type": "Attribute",
            "required": True,
        },
    )
    single_char: Optional[str] = field(
        default=None,
        metadata={
            "name": "singleChar",
            "type": "Attribute",
            "required": True,
        },
    )
    escape_char: Optional[str] = field(
        default=None,
        metadata={
            "name": "escapeChar",
            "type": "Attribute",
            "required": True,
        },
    )
    match_case: bool = field(
        default=True,
        metadata={
            "name": "matchCase",
            "type": "Attribute",
        },
    )
