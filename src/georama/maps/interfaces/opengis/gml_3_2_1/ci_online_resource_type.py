from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_on_line_function_code_property_type import (
    CiOnLineFunctionCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.url_property_type import UrlPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiOnlineResourceType(AbstractObjectType):
    """
    Information about online sources from which the dataset, specification, or
    community profile name and extended metadata elements can be obtained.
    """

    class Meta:
        name = "CI_OnlineResource_Type"

    linkage: UrlPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    protocol: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    application_profile: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "applicationProfile",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    name: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    function: CiOnLineFunctionCodePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
