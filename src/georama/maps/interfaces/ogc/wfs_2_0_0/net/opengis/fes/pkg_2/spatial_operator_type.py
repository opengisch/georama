from dataclasses import dataclass, field
from typing import Optional, Union

from wfs_2_0_0.net.opengis.fes.pkg_2.geometry_operands_type import GeometryOperandsType
from wfs_2_0_0.net.opengis.fes.pkg_2.spatial_operator_name_type_value import (
    SpatialOperatorNameTypeValue,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SpatialOperatorType:
    geometry_operands: Optional[GeometryOperandsType] = field(
        default=None,
        metadata={
            "name": "GeometryOperands",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    name: Optional[Union[str, SpatialOperatorNameTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"extension:\w{2,}",
        },
    )
