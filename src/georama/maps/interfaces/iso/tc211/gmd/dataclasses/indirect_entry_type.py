from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_proxy import (
    DefinitionProxy,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IndirectEntryType:
    definition_proxy: DefinitionProxy | None = field(
        default=None,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
