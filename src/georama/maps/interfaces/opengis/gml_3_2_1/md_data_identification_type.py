from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_md_identification_type import (
    AbstractMdIdentificationType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ex_extent_property_type import (
    ExExtentPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_character_set_code_property_type import (
    MdCharacterSetCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_resolution_property_type import (
    MdResolutionPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_spatial_representation_type_code_property_type import (
    MdSpatialRepresentationTypeCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_topic_category_code_property_type import (
    MdTopicCategoryCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDataIdentificationType(AbstractMdIdentificationType):
    class Meta:
        name = "MD_DataIdentification_Type"

    spatial_representation_type: list[MdSpatialRepresentationTypeCodePropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "spatialRepresentationType",
                "type": "Element",
                "namespace": "http://www.isotc211.org/2005/gmd",
            },
        )
    )
    spatial_resolution: list[MdResolutionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialResolution",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    language: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    character_set: list[MdCharacterSetCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "characterSet",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    topic_category: list[MdTopicCategoryCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "topicCategory",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    environment_description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "environmentDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    extent: list[ExExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    supplemental_information: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "supplementalInformation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
