from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gmltype import (
    AbstractGmltype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionType(AbstractGmltype):
    """A definition, which can be included in or referenced by a dictionary.

    In this extended type, the inherited "description" optional element can hold the definition whenever only text is needed. The inherited "name" elements can provide one or more brief terms for which this is the definition. The inherited "metaDataProperty" elements can be used to reference or include more information about this definition.
    The gml:id attribute is required - it must be possible to reference this definition using this handle.
    """

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
