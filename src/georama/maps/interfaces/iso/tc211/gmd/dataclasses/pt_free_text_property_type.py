from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pt_free_text import PtFreeText

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtFreeTextPropertyType(CharacterStringPropertyType):
    class Meta:
        name = "PT_FreeText_PropertyType"

    pt_free_text: Optional[PtFreeText] = field(
        default=None,
        metadata={
            "name": "PT_FreeText",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
