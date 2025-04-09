from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_temporal_validity_type import (
    DqTemporalValidityType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqTemporalValidity(DqTemporalValidityType):
    class Meta:
        name = "DQ_TemporalValidity"
        namespace = "http://www.isotc211.org/2005/gmd"
