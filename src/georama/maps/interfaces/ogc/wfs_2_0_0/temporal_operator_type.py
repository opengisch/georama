from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.temporal_operands_type import (
    TemporalOperandsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.temporal_operator_name_type_value import (
    TemporalOperatorNameTypeValue,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class TemporalOperatorType:
    temporal_operands: TemporalOperandsType | None = field(
        default=None,
        metadata={
            "name": "TemporalOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    name: str | TemporalOperatorNameTypeValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"extension:\w{2,}",
        },
    )
