from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.boolean_property_type_2 import (
    BooleanPropertyType2,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.gm_point_property_type import (
    GmPointPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_grid_spatial_representation_type import (
    MdGridSpatialRepresentationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_pixel_orientation_code_property_type import (
    MdPixelOrientationCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeorectifiedType(MdGridSpatialRepresentationType):
    class Meta:
        name = "MD_Georectified_Type"

    check_point_availability: BooleanPropertyType2 | None = field(
        default=None,
        metadata={
            "name": "checkPointAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    check_point_description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "checkPointDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    corner_points: list[GmPointPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "cornerPoints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    center_point: GmPointPropertyType | None = field(
        default=None,
        metadata={
            "name": "centerPoint",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    point_in_pixel: MdPixelOrientationCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "pointInPixel",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    transformation_dimension_description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "transformationDimensionDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    transformation_dimension_mapping: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "transformationDimensionMapping",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "max_occurs": 2,
        },
    )
