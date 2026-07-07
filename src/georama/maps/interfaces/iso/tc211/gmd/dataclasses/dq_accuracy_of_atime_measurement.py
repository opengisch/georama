from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_accuracy_of_atime_measurement_type import (
    DqAccuracyOfAtimeMeasurementType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqAccuracyOfAtimeMeasurement(DqAccuracyOfAtimeMeasurementType):
    class Meta:
        name = "DQ_AccuracyOfATimeMeasurement"
        namespace = "http://www.isotc211.org/2005/gmd"
