from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.function_names_type import (
    FunctionNamesType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FunctionsType:
    function_names: FunctionNamesType | None = field(
        default=None,
        metadata={
            "name": "FunctionNames",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        },
    )
