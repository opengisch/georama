from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.integer_property_type import (
    IntegerPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_medium_format_code_property_type import (
    MdMediumFormatCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_medium_name_code_property_type import (
    MdMediumNameCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.real_property_type import (
    RealPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMediumType(AbstractObjectType):
    """
    Information about the media on which the data can be distributed.
    """

    class Meta:
        name = "MD_Medium_Type"

    name: MdMediumNameCodePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    density: list[RealPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    density_units: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "densityUnits",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    volumes: IntegerPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    medium_format: list[MdMediumFormatCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "mediumFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    medium_note: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "mediumNote",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
