from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_coverage_type import (
    AbstractCoverageType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.coverage_function import CoverageFunction

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DiscreteCoverageType(AbstractCoverageType):
    coverage_function: CoverageFunction | None = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
