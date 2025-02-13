from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.fes.pkg_2.available_function_type import (
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
