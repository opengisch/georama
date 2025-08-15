from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.temporal_csref_type import (
    TemporalCsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesTemporalCs(TemporalCsrefType):
    """
    Association to the temporal coordinate system used by this CRS.
    """

    class Meta:
        name = "usesTemporalCS"
        namespace = "http://www.opengis.net/gml"
