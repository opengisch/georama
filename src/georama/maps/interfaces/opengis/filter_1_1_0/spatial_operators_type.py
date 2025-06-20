from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.spatial_operator_type import (
    SpatialOperatorType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SpatialOperatorsType:
    spatial_operator: list[SpatialOperatorType] = field(
        default_factory=list,
        metadata={
            "name": "SpatialOperator",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 1,
        },
    )
