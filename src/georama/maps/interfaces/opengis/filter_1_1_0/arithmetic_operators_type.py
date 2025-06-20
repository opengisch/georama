from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.functions_type import FunctionsType
from georama.maps.interfaces.opengis.filter_1_1_0.simple_arithmetic import (
    SimpleArithmetic,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class ArithmeticOperatorsType:
    simple_arithmetic: list[SimpleArithmetic] = field(
        default_factory=list,
        metadata={
            "name": "SimpleArithmetic",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    functions: list[FunctionsType] = field(
        default_factory=list,
        metadata={
            "name": "Functions",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
