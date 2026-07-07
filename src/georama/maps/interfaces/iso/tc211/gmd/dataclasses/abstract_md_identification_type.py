from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_aggregate_information_property_type import (
    MdAggregateInformationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_browse_graphic_property_type import (
    MdBrowseGraphicPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_constraints_property_type import (
    MdConstraintsPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_distributor_type import (
    MdFormatPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_identifier_type import (
    CiCitationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_keywords_property_type import (
    MdKeywordsPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_maintenance_information_property_type import (
    MdMaintenanceInformationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_progress_code_property_type import (
    MdProgressCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_usage_property_type import (
    MdUsagePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractMdIdentificationType(AbstractObjectType):
    """
    Basic information about data.
    """

    class Meta:
        name = "AbstractMD_Identification_Type"

    citation: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    abstract: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    purpose: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    credit: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    status: List[MdProgressCodePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    point_of_contact: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "pointOfContact",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    resource_maintenance: List[MdMaintenanceInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceMaintenance",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    graphic_overview: List[MdBrowseGraphicPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "graphicOverview",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    resource_format: List[MdFormatPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    descriptive_keywords: List[MdKeywordsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "descriptiveKeywords",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    resource_specific_usage: List[MdUsagePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceSpecificUsage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    resource_constraints: List[MdConstraintsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "resourceConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    aggregation_info: List[MdAggregateInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "aggregationInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
