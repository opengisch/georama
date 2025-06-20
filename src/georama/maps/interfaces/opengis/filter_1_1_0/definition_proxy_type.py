from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.definition_ref import DefinitionRef
from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionProxyType(DefinitionType):
    """A proxy entry in a dictionary of definitions.

    An element of this type contains a reference to a remote definition
    object. This entry is expected to be convenient in allowing multiple
    elements in one XML document to contain short (abbreviated XPointer)
    references, which are resolved to an external definition provided in
    a Dictionary element in the same XML document.

    :ivar definition_ref: A reference to a remote entry in this
        dictionary, used when this dictionary entry is identified to
        allow external references to this specific entry. The remote
        entry referenced can be in a dictionary in the same or different
        XML document.
    """

    definition_ref: Optional[DefinitionRef] = field(
        default=None,
        metadata={
            "name": "definitionRef",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
