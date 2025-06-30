from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.comparison_operators_type import (
    ComparisonOperatorsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.logical_operators import LogicalOperators

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ScalarCapabilitiesType:
    class Meta:
        name = "Scalar_CapabilitiesType"

    logical_operators: Optional[LogicalOperators] = field(
        default=None,
        metadata={
            "name": "LogicalOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    comparison_operators: Optional[ComparisonOperatorsType] = field(
        default=None,
        metadata={
            "name": "ComparisonOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
