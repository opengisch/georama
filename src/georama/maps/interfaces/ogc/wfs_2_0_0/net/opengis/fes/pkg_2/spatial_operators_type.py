from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.spatial_operator_type import (
    SpatialOperatorType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SpatialOperatorsType:
    spatial_operator: list[SpatialOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "SpatialOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
