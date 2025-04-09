from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.domain_type import (
    DomainType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ConformanceType:
    constraint: list[DomainType] = field(
        default_factory=list,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
