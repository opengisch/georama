from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_continuous_coverage_type import (
    AbstractContinuousCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractContinuousCoverage(AbstractContinuousCoverageType):
    """A continuous coverage as defined in ISO 19123 is a coverage that can return
    different values for the same feature attribute at different direct positions
    within a single spatiotemporal object in its spatiotemporal domain.

    The base type for continuous coverages is
    AbstractContinuousCoverageType. The coverageFunction element
    describes the mapping function. The abstract element
    gml:AbstractContinuousCoverage serves as the head of a substitution
    group which may contain any continuous coverage whose type is
    derived from gml:AbstractContinuousCoverageType.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
