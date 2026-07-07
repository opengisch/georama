from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_thematic_classification_correctness_type import (
    DqThematicClassificationCorrectnessType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqThematicClassificationCorrectness(DqThematicClassificationCorrectnessType):
    class Meta:
        name = "DQ_ThematicClassificationCorrectness"
        namespace = "http://www.isotc211.org/2005/gmd"
