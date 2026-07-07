from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.localised_character_string_type import (
    LocalisedCharacterStringType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LocalisedCharacterString(LocalisedCharacterStringType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gmd"
