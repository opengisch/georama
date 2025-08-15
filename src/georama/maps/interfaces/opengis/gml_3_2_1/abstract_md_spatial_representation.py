from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_md_spatial_representation_type import (
    AbstractMdSpatialRepresentationType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractMdSpatialRepresentation(AbstractMdSpatialRepresentationType):
    class Meta:
        name = "AbstractMD_SpatialRepresentation"
        namespace = "http://www.isotc211.org/2005/gmd"
