from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.array_type import AbstractCoverageType
from georama.maps.interfaces.opengis.filter_1_1_0.coverage_function import (
    CoverageFunction,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractContinuousCoverageType(AbstractCoverageType):
    """
    A continuous coverage as defined in ISO 19123 is a coverage that can return
    different values for the same feature attribute at different direct positions
    within a single spatiotemporal object in its spatiotemporal domain.
    """

    coverage_function: Optional[CoverageFunction] = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
