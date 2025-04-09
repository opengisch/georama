from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_classification_code_property_type import (
    MdClassificationCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_constraints_type import (
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

    classification: Optional[MdClassificationCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    user_note: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "userNote",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    classification_system: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "classificationSystem",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    handling_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "handlingDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
