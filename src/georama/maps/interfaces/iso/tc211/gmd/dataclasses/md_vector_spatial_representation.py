from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_vector_spatial_representation_type import (
    MdVectorSpatialRepresentationType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdVectorSpatialRepresentation(MdVectorSpatialRepresentationType):
    class Meta:
        name = "MD_VectorSpatialRepresentation"
        namespace = "http://www.isotc211.org/2005/gmd"
