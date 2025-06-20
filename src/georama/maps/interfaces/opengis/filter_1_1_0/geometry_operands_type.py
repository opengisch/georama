from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.geometry_operand_type import (
    GeometryOperandType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class GeometryOperandsType:
    geometry_operand: list[GeometryOperandType] = field(
        default_factory=list,
        metadata={
            "name": "GeometryOperand",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        },
    )
