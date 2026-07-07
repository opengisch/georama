from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_dq_temporal_accuracy_type import (
    AbstractDqTemporalAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqTemporalValidityType(AbstractDqTemporalAccuracyType):
    class Meta:
        name = "DQ_TemporalValidity_Type"
