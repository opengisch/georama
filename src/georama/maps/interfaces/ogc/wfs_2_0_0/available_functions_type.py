from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.available_function_type import (
    AvailableFunctionType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AvailableFunctionsType:
    function: list[AvailableFunctionType] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
