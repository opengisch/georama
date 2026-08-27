from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_date_property_type import (
    CiDatePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.localised_character_string_property_type import (
    LocalisedCharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.pt_locale_property_type import (
    PtLocalePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtLocaleContainerType:
    class Meta:
        name = "PT_LocaleContainer_Type"

    description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    locale: PtLocalePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    date: list[CiDatePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    responsible_party: list[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    localised_string: list[LocalisedCharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "localisedString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
