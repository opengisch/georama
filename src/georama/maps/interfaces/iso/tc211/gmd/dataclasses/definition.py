from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_type import (
    DefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Definition(DefinitionType):
    """The basic gml:Definition element specifies a definition, which can be
    included in or referenced by a dictionary.

    The content model for a generic definition is a derivation from
    gml:AbstractGMLType. The gml:description property element shall hold
    the definition if this can be captured in a simple text string, or
    the gml:descriptionReference property element may carry a link to a
    description elsewhere. The gml:identifier element shall provide one
    identifier identifying this definition. The identifier shall be
    unique within the dictionaries using this definition. The gml:name
    elements shall provide zero or more terms and synonyms for which
    this is the definition. The gml:remarks element shall be used to
    hold additional textual information that is not conceptually part of
    the definition but is useful in understanding the definition.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
