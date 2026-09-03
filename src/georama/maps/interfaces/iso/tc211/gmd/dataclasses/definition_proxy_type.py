from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_ref import (
    DefinitionRef,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_type import (
    DefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionProxyType(DefinitionType):
    definition_ref: DefinitionRef | None = field(
        default=None,
        metadata={
            "name": "definitionRef",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
