from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.dq_topological_consistency_type import (
    DqTopologicalConsistencyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqTopologicalConsistency(DqTopologicalConsistencyType):
    class Meta:
        name = "DQ_TopologicalConsistency"
        namespace = "http://www.isotc211.org/2005/gmd"
