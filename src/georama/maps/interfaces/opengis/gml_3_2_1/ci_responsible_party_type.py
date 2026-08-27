from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_contact_property_type import (
    CiContactPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_role_code_property_type import (
    CiRoleCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiResponsiblePartyType(AbstractObjectType):
    """
    Identification of, and means of communication with, person(s) and organisations
    associated with the dataset.
    """

    class Meta:
        name = "CI_ResponsibleParty_Type"

    individual_name: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "individualName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    organisation_name: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "organisationName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    position_name: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "positionName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    contact_info: CiContactPropertyType | None = field(
        default=None,
        metadata={
            "name": "contactInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    role: CiRoleCodePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
