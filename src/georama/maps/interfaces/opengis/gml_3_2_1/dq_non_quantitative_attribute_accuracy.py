from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.dq_non_quantitative_attribute_accuracy_type import (
    DqNonQuantitativeAttributeAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqNonQuantitativeAttributeAccuracy(DqNonQuantitativeAttributeAccuracyType):
    class Meta:
        name = "DQ_NonQuantitativeAttributeAccuracy"
        namespace = "http://www.isotc211.org/2005/gmd"
