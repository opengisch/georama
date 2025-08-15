from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_dq_positional_accuracy_type import (
    AbstractDqPositionalAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqAbsoluteExternalPositionalAccuracyType(AbstractDqPositionalAccuracyType):
    class Meta:
        name = "DQ_AbsoluteExternalPositionalAccuracy_Type"
