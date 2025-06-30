from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.ogc.wfs_2_0_0.function_type import Function
from georama.maps.interfaces.ogc.wfs_2_0_0.literal import Literal
from georama.maps.interfaces.ogc.wfs_2_0_0.value_reference import ValueReference

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class LowerBoundaryType:
    literal_or_function_or_value_reference: Optional[
        Union[Literal, Function, ValueReference]
    ] = field(
        default=None,
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
                    "type": Function,
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
