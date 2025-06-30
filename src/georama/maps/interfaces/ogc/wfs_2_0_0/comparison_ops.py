from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.comparison_ops_type import ComparisonOpsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ComparisonOps(ComparisonOpsType):
    class Meta:
        name = "comparisonOps"
        namespace = "http://www.opengis.net/fes/2.0"
