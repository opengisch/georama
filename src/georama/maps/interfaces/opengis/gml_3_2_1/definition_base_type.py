from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_gmltype import AbstractGmltype
from georama.maps.interfaces.opengis.gml_3_2_1.identifier import Identifier

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinitionBaseType(AbstractGmltype):
    identifier: Identifier | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
