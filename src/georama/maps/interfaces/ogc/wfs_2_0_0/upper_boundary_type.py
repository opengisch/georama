from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.function_type import Function
from georama.maps.interfaces.ogc.wfs_2_0_0.literal import Literal
from georama.maps.interfaces.ogc.wfs_2_0_0.value_reference import ValueReference

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class UpperBoundaryType:
    literal_or_function_or_value_reference: (
        Literal | Function | ValueReference | None
    ) = field(
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
