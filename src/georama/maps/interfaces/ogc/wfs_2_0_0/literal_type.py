from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class LiteralType:
    type_value: QName | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
