from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.object_reference_property_type import (
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

    attributes: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    features: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    feature_instances: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureInstances",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    attribute_instances: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "attributeInstances",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dataset: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    other: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
