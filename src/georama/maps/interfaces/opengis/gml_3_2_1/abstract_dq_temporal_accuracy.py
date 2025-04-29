from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_dq_temporal_accuracy_type import (
    AbstractDqTemporalAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqTemporalAccuracy(AbstractDqTemporalAccuracyType):
    class Meta:
        name = "AbstractDQ_TemporalAccuracy"
        namespace = "http://www.isotc211.org/2005/gmd"
