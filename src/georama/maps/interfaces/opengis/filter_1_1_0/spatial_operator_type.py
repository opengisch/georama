from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.geometry_operands_type import (
    GeometryOperandsType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.spatial_operator_name_type import (
    SpatialOperatorNameType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SpatialOperatorType:
    geometry_operands: GeometryOperandsType | None = field(
        default=None,
        metadata={
            "name": "GeometryOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    name: SpatialOperatorNameType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
