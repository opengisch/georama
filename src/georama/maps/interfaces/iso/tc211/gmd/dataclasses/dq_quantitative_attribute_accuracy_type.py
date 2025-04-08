from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_dq_thematic_accuracy_type import (
    AbstractDqThematicAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqQuantitativeAttributeAccuracyType(AbstractDqThematicAccuracyType):
    class Meta:
        name = "DQ_QuantitativeAttributeAccuracy_Type"
