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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.date_property_type import (
    DatePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_maintenance_frequency_code_property_type import (
    MdMaintenanceFrequencyCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_scope_code_property_type import (
    MdScopeCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_scope_description_property_type import (
    MdScopeDescriptionPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.tm_period_duration_property_type import (
    TmPeriodDurationPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMaintenanceInformationType(AbstractObjectType):
    """
    Information about the scope and frequency of updating.
    """

    class Meta:
        name = "MD_MaintenanceInformation_Type"

    maintenance_and_update_frequency: MdMaintenanceFrequencyCodePropertyType | None = (
        field(
            default=None,
            metadata={
                "name": "maintenanceAndUpdateFrequency",
                "type": "Element",
                "namespace": "http://www.isotc211.org/2005/gmd",
                "required": True,
            },
        )
    )
    date_of_next_update: DatePropertyType | None = field(
        default=None,
        metadata={
            "name": "dateOfNextUpdate",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    user_defined_maintenance_frequency: TmPeriodDurationPropertyType | None = field(
        default=None,
        metadata={
            "name": "userDefinedMaintenanceFrequency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    update_scope: list[MdScopeCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "updateScope",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    update_scope_description: list[MdScopeDescriptionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "updateScopeDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    maintenance_note: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "maintenanceNote",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    contact: list[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
