from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.arithmetic_operators_type import (
    ArithmeticOperatorsType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.comparison_operators_type import (
    ComparisonOperatorsType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.logical_operators import (
    LogicalOperators,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class ScalarCapabilitiesType:
    class Meta:
        name = "Scalar_CapabilitiesType"

    logical_operators: LogicalOperators | None = field(
        default=None,
        metadata={
            "name": "LogicalOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    comparison_operators: ComparisonOperatorsType | None = field(
        default=None,
        metadata={
            "name": "ComparisonOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    arithmetic_operators: ArithmeticOperatorsType | None = field(
        default=None,
        metadata={
            "name": "ArithmeticOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
