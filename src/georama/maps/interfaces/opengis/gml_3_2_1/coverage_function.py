from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.coverage_function_type import (
    CoverageFunctionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoverageFunction(CoverageFunctionType):
    """The gml:coverageFunction property describes the mapping function from the
    domain to the range of the coverage.

    The value of the CoverageFunction is one of gml:CoverageMappingRule
    and gml:GridFunction. If the gml:coverageFunction property is
    omitted for a gridded coverage (including rectified gridded
    coverages) the gml:startPoint is assumed to be the value of the
    gml:low property in the gml:Grid geometry, and the gml:sequenceRule
    is assumed to be linear and the gml:axisOrder property is assumed to
    be "+1 +2".
    """

    class Meta:
        name = "coverageFunction"
        namespace = "http://www.opengis.net/gml/3.2"
