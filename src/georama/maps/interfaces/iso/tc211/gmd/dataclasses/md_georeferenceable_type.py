from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.boolean_property_type_2 import (
    BooleanPropertyType2,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_grid_spatial_representation_type import (
    MdGridSpatialRepresentationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_identifier_type import (
    CiCitationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.record_property_type import (
    RecordPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeoreferenceableType(MdGridSpatialRepresentationType):
    class Meta:
        name = "MD_Georeferenceable_Type"

    control_point_availability: BooleanPropertyType2 | None = field(
        default=None,
        metadata={
            "name": "controlPointAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    orientation_parameter_availability: BooleanPropertyType2 | None = field(
        default=None,
        metadata={
            "name": "orientationParameterAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    orientation_parameter_description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "orientationParameterDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    georeferenced_parameters: RecordPropertyType | None = field(
        default=None,
        metadata={
            "name": "georeferencedParameters",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    parameter_citation: list[CiCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "parameterCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
