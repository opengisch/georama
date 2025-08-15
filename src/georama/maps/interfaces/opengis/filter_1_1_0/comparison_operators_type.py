from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.comparison_operator_type import (
    ComparisonOperatorType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class ComparisonOperatorsType:
    comparison_operator: list[ComparisonOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "ComparisonOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        },
    )
