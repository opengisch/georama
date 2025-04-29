from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.md_grid_spatial_representation_type import (
    MdGridSpatialRepresentationType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGridSpatialRepresentation(MdGridSpatialRepresentationType):
    class Meta:
        name = "MD_GridSpatialRepresentation"
        namespace = "http://www.isotc211.org/2005/gmd"
