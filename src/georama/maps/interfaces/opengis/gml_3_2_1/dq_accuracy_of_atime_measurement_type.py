from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_dq_temporal_accuracy_type import (
    AbstractDqTemporalAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqAccuracyOfAtimeMeasurementType(AbstractDqTemporalAccuracyType):
    class Meta:
        name = "DQ_AccuracyOfATimeMeasurement_Type"
