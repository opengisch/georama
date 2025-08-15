from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.ex_spatial_temporal_extent_type import (
    ExSpatialTemporalExtentType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExSpatialTemporalExtent(ExSpatialTemporalExtentType):
    class Meta:
        name = "EX_SpatialTemporalExtent"
        namespace = "http://www.isotc211.org/2005/gmd"
