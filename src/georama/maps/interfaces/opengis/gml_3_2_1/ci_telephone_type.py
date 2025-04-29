from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiTelephoneType(AbstractObjectType):
    """
    Telephone numbers for contacting the responsible individual or organisation.
    """

    class Meta:
        name = "CI_Telephone_Type"

    voice: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    facsimile: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
