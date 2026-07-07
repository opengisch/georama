from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.ex_geographic_extent_property_type import (
    ExGeographicExtentPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ex_temporal_extent_type import (
    ExTemporalExtentType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExSpatialTemporalExtentType(ExTemporalExtentType):
    """
    Extent with respect to date and time.
    """

    class Meta:
        name = "EX_SpatialTemporalExtent_Type"

    spatial_extent: list[ExGeographicExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialExtent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
