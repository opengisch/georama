from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.definition_proxy import DefinitionProxy

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class IndirectEntryType:
    definition_proxy: DefinitionProxy | None = field(
        default=None,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
