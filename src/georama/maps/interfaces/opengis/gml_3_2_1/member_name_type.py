from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.type_name_property_type import (
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

    a_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "aName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "required": True,
        },
    )
    attribute_type: Optional[TypeNamePropertyType] = field(
        default=None,
        metadata={
            "name": "attributeType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "required": True,
        },
    )
