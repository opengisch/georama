from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_continuous_coverage_type import (
    AbstractContinuousCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ContinuousCoverage(AbstractContinuousCoverageType):
    class Meta:
        name = "_ContinuousCoverage"
        namespace = "http://www.opengis.net/gml"
