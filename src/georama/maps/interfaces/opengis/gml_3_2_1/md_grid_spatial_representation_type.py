from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_md_spatial_representation_type import (
    AbstractMdSpatialRepresentationType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.boolean_property_type_2 import (
    BooleanPropertyType2,
)
from georama.maps.interfaces.opengis.gml_3_2_1.integer_property_type import (
    IntegerPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_cell_geometry_code_property_type import (
    MdCellGeometryCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_dimension_property_type import (
    MdDimensionPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGridSpatialRepresentationType(AbstractMdSpatialRepresentationType):
    """
    Types and numbers of raster spatial objects in the dataset.
    """

    class Meta:
        name = "MD_GridSpatialRepresentation_Type"

    number_of_dimensions: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "numberOfDimensions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    axis_dimension_properties: list[MdDimensionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "axisDimensionProperties",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    cell_geometry: Optional[MdCellGeometryCodePropertyType] = field(
        default=None,
        metadata={
            "name": "cellGeometry",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    transformation_parameter_availability: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "transformationParameterAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
