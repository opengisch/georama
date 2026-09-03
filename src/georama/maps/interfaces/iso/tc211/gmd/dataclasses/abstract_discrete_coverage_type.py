from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_coverage_type import (
    AbstractCoverageType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coverage_function import (
    CoverageFunction,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractDiscreteCoverageType(AbstractCoverageType):
    coverage_function: CoverageFunction | None = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
