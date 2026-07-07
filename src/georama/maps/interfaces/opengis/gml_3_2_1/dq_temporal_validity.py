from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.dq_temporal_validity_type import (
    DqTemporalValidityType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqTemporalValidity(DqTemporalValidityType):
    class Meta:
        name = "DQ_TemporalValidity"
        namespace = "http://www.isotc211.org/2005/gmd"
