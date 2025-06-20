from dataclasses import dataclass, field
from typing import Optional

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

    logical_operators: Optional[LogicalOperators] = field(
        default=None,
        metadata={
            "name": "LogicalOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    comparison_operators: Optional[ComparisonOperatorsType] = field(
        default=None,
        metadata={
            "name": "ComparisonOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    arithmetic_operators: Optional[ArithmeticOperatorsType] = field(
        default=None,
        metadata={
            "name": "ArithmeticOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
