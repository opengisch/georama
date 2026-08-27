from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.type_name_property_type import (
    TypeNamePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MemberNameType(AbstractObjectType):
    """A MemberName is a LocalName that references either an attribute slot in a
    record or  recordType or an attribute, operation, or association role in an
    object instance or  type description in some form of schema.

    The stored value "aName" is the returned value for the "aName()"
    operation.
    """

    class Meta:
        name = "MemberName_Type"

    a_name: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "aName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "required": True,
        },
    )
    attribute_type: TypeNamePropertyType | None = field(
        default=None,
        metadata={
            "name": "attributeType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "required": True,
        },
    )
