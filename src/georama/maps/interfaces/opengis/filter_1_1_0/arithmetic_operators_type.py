from dataclasses import dataclass, field
from typing import Union

from georama.maps.interfaces.opengis.filter_1_1_0.functions_type import FunctionsType
from georama.maps.interfaces.opengis.filter_1_1_0.simple_arithmetic import (
    SimpleArithmetic,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class ArithmeticOperatorsType:
    simple_arithmetic_or_functions: list[Union[SimpleArithmetic, FunctionsType]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleArithmetic",
                    "type": SimpleArithmetic,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Functions",
                    "type": FunctionsType,
                    "namespace": "http://www.opengis.net/ogc",
                },
            ),
        },
    )
