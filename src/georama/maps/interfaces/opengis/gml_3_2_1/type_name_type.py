from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class TypeNameType(AbstractObjectType):
    """A TypeName is a LocalName that references either a recordType or object type
    in some form of schema.

    The stored value "aName" is the returned value for the "aName()" operation. This is the types name.  - For parsing from types (or objects) the parsible name normally uses a "." navigation separator, so that it is of the form  [class].[member].[memberOfMember]. ...)
    """

    class Meta:
        name = "TypeName_Type"

    a_name: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "aName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "required": True,
        },
    )
