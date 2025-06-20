from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.coverage_function_type import (
    CoverageFunctionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoverageFunction(CoverageFunctionType):
    class Meta:
        name = "coverageFunction"
        namespace = "http://www.opengis.net/gml"
