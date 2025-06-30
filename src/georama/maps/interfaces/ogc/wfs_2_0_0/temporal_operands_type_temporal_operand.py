from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class TemporalOperandsTypeTemporalOperand:
    class Meta:
        global_type = False

    name: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
