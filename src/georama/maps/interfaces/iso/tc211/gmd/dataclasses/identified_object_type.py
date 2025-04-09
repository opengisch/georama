from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_type import (
    DefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IdentifiedObjectType(DefinitionType):
    """Gml:IdentifiedObjectType provides identification properties of a CRS-related
    object.

    In gml:DefinitionType, the gml:identifier element shall be the
    primary name by which this object is identified, encoding the "name"
    attribute in the UML model. Zero or more of the gml:name elements
    can be an unordered set of "identifiers", encoding the "identifier"
    attribute in the UML model. Each of these gml:name elements can
    reference elsewhere the object's defining information or be an
    identifier by which this object can be referenced. Zero or more
    other gml:name elements can be an unordered set of "alias"
    alternative names by which this CRS related object is identified,
    encoding the "alias" attributes in the UML model. An object may have
    several aliases, typically used in different contexts. The context
    for an alias is indicated by the value of its (optional) codeSpace
    attribute. Any needed version information shall be included in the
    codeSpace attribute of a gml:identifier and gml:name elements. In
    this use, the gml:remarks element in the gml:DefinitionType shall
    contain comments on or information about this object, including data
    source information.
    """
