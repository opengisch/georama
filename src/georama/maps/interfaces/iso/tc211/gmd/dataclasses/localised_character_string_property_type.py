from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.localised_character_string import (
    LocalisedCharacterString,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.object_reference_property_type import (
    ObjectReferencePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LocalisedCharacterStringPropertyType(ObjectReferencePropertyType):
    class Meta:
        name = "LocalisedCharacterString_PropertyType"

    localised_character_string: LocalisedCharacterString | None = field(
        default=None,
        metadata={
            "name": "LocalisedCharacterString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
