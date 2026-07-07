from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.temporal_operands_type_temporal_operand import (
    TemporalOperandsTypeTemporalOperand,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class TemporalOperandsType:
    temporal_operand: list[TemporalOperandsTypeTemporalOperand] = field(
        default_factory=list,
        metadata={
            "name": "TemporalOperand",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
