from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.comparison_operator_type import (
    ComparisonOperatorType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ComparisonOperatorsType:
    comparison_operator: list[ComparisonOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "ComparisonOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
