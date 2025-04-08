from dataclasses import dataclass, field
from typing import List

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_constraints_type import (
    MdConstraintsType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_restriction_code_property_type import (
    MdRestrictionCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdLegalConstraintsType(MdConstraintsType):
    """
    Restrictions and legal prerequisites for accessing and using the dataset.
    """

    class Meta:
        name = "MD_LegalConstraints_Type"

    access_constraints: List[MdRestrictionCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "accessConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    use_constraints: List[MdRestrictionCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "useConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    other_constraints: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "otherConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
