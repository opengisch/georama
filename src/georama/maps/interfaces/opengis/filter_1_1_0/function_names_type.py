from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.function_name_type import (
    FunctionNameType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FunctionNamesType:
    function_name: list[FunctionNameType] = field(
        default_factory=list,
        metadata={
            "name": "FunctionName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        },
    )
