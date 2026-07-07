from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_temporal_consistency_type import (
    DqTemporalConsistencyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqTemporalConsistency(DqTemporalConsistencyType):
    class Meta:
        name = "DQ_TemporalConsistency"
        namespace = "http://www.isotc211.org/2005/gmd"
