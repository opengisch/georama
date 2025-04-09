from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
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

    file_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    file_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    file_type: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
