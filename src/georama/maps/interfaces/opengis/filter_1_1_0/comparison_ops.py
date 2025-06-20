from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.comparison_ops_type import (
    ComparisonOpsType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class ComparisonOps(ComparisonOpsType):
    class Meta:
        name = "comparisonOps"
        namespace = "http://www.opengis.net/ogc"
