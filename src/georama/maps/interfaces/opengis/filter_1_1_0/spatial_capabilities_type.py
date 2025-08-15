from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.geometry_operands_type import (
    GeometryOperandsType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.spatial_operators_type import (
    SpatialOperatorsType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SpatialCapabilitiesType:
    class Meta:
        name = "Spatial_CapabilitiesType"

    geometry_operands: Optional[GeometryOperandsType] = field(
        default=None,
        metadata={
            "name": "GeometryOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        },
    )
    spatial_operators: Optional[SpatialOperatorsType] = field(
        default=None,
        metadata={
            "name": "SpatialOperators",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        },
    )
