from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.definition_proxy import (
    DefinitionProxy,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IndirectEntryType:
    """An entry in a dictionary of definitions that contains a GML object which
    references a remote definition object.

    This entry is expected to be convenient in allowing multiple
    elements in one XML document to contain short (abbreviated XPointer)
    references, which are resolved to an external definition provided in
    a Dictionary element in the same XML document. Specialized
    descendents of this dictionaryEntry might be restricted in an
    application schema to allow only including specified types of
    definitions as valid entries in a dictionary.
    """

    definition_proxy: Optional[DefinitionProxy] = field(
        default=None,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
