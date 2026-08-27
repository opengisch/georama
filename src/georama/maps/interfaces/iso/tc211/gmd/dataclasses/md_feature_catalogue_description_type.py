from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_md_content_information_type import (
    AbstractMdContentInformationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.boolean_property_type_2 import (
    BooleanPropertyType2,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.generic_name_property_type import (
    GenericNamePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_identifier_type import (
    CiCitationPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdFeatureCatalogueDescriptionType(AbstractMdContentInformationType):
    """
    Information identifing the feature catalogue.
    """

    class Meta:
        name = "MD_FeatureCatalogueDescription_Type"

    compliance_code: BooleanPropertyType2 | None = field(
        default=None,
        metadata={
            "name": "complianceCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    language: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    included_with_dataset: BooleanPropertyType2 | None = field(
        default=None,
        metadata={
            "name": "includedWithDataset",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    feature_types: list[GenericNamePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureTypes",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    feature_catalogue_citation: list[CiCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureCatalogueCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
