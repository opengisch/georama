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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.integer_property_type import (
    IntegerPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_datatype_code_property_type import (
    MdDatatypeCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_obligation_code_property_type import (
    MdObligationCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdExtendedElementInformationType(AbstractObjectType):
    """
    New metadata element, not found in ISO 19115, which is required to describe
    geographic data.
    """

    class Meta:
        name = "MD_ExtendedElementInformation_Type"

    name: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    short_name: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    domain_code: IntegerPropertyType | None = field(
        default=None,
        metadata={
            "name": "domainCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    definition: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    obligation: MdObligationCodePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    condition: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    data_type: MdDatatypeCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "dataType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    maximum_occurrence: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "maximumOccurrence",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    domain_value: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "domainValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    parent_entity: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "parentEntity",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    rule: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    rationale: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source: list[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
