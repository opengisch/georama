from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class GeometryOperandsType:
    geometry_operand: list["GeometryOperandsType.GeometryOperand"] = field(
        default_factory=list,
        metadata={
            "name": "GeometryOperand",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )

    @dataclass
    class GeometryOperand:
        name: Optional[QName] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
