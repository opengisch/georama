from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_identifier_type import (
    CiCitationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_keyword_type_code_property_type import (
    MdKeywordTypeCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdKeywordsType(AbstractObjectType):
    """
    Keywords, their type and reference source.
    """

    class Meta:
        name = "MD_Keywords_Type"

    keyword: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    type_value: MdKeywordTypeCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    thesaurus_name: CiCitationPropertyType | None = field(
        default=None,
        metadata={
            "name": "thesaurusName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
