from dataclasses import dataclass, field
from typing import Any, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_discrete_coverage_type import (
    AbstractDiscreteCoverageType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_point_domain import (
    MultiPointDomain,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPointCoverageType(AbstractDiscreteCoverageType):
    rectified_grid_domain: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    grid_domain: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid_domain: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    multi_surface_domain: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve_domain: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    domain_set: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    location: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    multi_point_domain: Optional[MultiPointDomain] = field(
        default=None,
        metadata={
            "name": "multiPointDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
