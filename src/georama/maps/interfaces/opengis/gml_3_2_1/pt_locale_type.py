from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.country_property_type import (
    CountryPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.language_code_property_type import (
    LanguageCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_character_set_code_property_type import (
    MdCharacterSetCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtLocaleType(AbstractObjectType):
    class Meta:
        name = "PT_Locale_Type"

    language_code: LanguageCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    country: CountryPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    character_encoding: MdCharacterSetCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "characterEncoding",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
