from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from georama.maps.interfaces.ogc.wfs_2_0_0.literal import Literal
from georama.maps.interfaces.ogc.wfs_2_0_0.value_reference import ValueReference

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class FunctionType:
    literal_or_function_or_value_reference: list[
        Union[Literal, "Function", ValueReference]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Literal",
                    "type": Literal,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Function",
                    "type": ForwardRef("Function"),
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "ValueReference",
                    "type": ValueReference,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
            ),
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Function(FunctionType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
