from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.dq_conceptual_consistency_type import (
    DqConceptualConsistencyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqConceptualConsistency(DqConceptualConsistencyType):
    class Meta:
        name = "DQ_ConceptualConsistency"
        namespace = "http://www.isotc211.org/2005/gmd"
