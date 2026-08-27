from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.object_reference_property_type import (
    ObjectReferencePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdScopeDescriptionType:
    """
    Description of the class of information covered by the information.
    """

    class Meta:
        name = "MD_ScopeDescription_Type"

    attributes: list[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    features: list[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    feature_instances: list[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureInstances",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    attribute_instances: list[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "attributeInstances",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dataset: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    other: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
