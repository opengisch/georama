from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_classification_code_property_type import (
    MdClassificationCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_constraints_type import (
    MdConstraintsType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdSecurityConstraintsType(MdConstraintsType):
    """
    Handling restrictions imposed on the dataset because of national security,
    privacy, or other concerns.
    """

    class Meta:
        name = "MD_SecurityConstraints_Type"

    classification: MdClassificationCodePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    user_note: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "userNote",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    classification_system: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "classificationSystem",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    handling_description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "handlingDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
