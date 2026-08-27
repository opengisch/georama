from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.date_time_property_type import (
    DateTimePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdUsageType(AbstractObjectType):
    """
    Brief description of ways in which the dataset is currently used.
    """

    class Meta:
        name = "MD_Usage_Type"

    specific_usage: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "specificUsage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    usage_date_time: DateTimePropertyType | None = field(
        default=None,
        metadata={
            "name": "usageDateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    user_determined_limitations: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "userDeterminedLimitations",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    user_contact_info: list[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "userContactInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
