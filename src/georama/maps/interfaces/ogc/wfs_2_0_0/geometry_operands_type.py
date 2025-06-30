from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.geometry_operands_type_geometry_operand import (
    GeometryOperandsTypeGeometryOperand,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class GeometryOperandsType:
    geometry_operand: list[GeometryOperandsTypeGeometryOperand] = field(
        default_factory=list,
        metadata={
            "name": "GeometryOperand",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
