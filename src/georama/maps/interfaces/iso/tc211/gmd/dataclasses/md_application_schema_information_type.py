from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.binary_property_type import (
    BinaryPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_identifier_type import (
    CiCitationPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdApplicationSchemaInformationType(AbstractObjectType):
    """
    Information about the application schema used to build the dataset.
    """

    class Meta:
        name = "MD_ApplicationSchemaInformation_Type"

    name: CiCitationPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    schema_language: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "schemaLanguage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    constraint_language: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "constraintLanguage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    schema_ascii: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "schemaAscii",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    graphics_file: BinaryPropertyType | None = field(
        default=None,
        metadata={
            "name": "graphicsFile",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    software_development_file: BinaryPropertyType | None = field(
        default=None,
        metadata={
            "name": "softwareDevelopmentFile",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    software_development_file_format: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "softwareDevelopmentFileFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
