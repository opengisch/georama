from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.definition_ref import DefinitionRef
from georama.maps.interfaces.opengis.gml_3_2_1.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinitionProxyType(DefinitionType):
    definition_ref: DefinitionRef | None = field(
        default=None,
        metadata={
            "name": "definitionRef",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
