from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdBrowseGraphicType(AbstractObjectType):
    """
    Graphic that provides an illustration of the dataset (should include a legend
    for the graphic)
    """

    class Meta:
        name = "MD_BrowseGraphic_Type"

    file_name: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    file_description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "fileDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    file_type: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "fileType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
