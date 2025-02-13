from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.fes.pkg_2.temporal_operator_type import TemporalOperatorType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class TemporalOperatorsType:
    temporal_operator: list[TemporalOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "TemporalOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
