from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class GeometryOperandsTypeGeometryOperand:
    class Meta:
        global_type = False

    name: QName | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
