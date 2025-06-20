from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.grid_type import GridType
from georama.maps.interfaces.opengis.filter_1_1_0.point_property_type import (
    PointPropertyType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridType(GridType):
    """
    A rectified grid has an origin and vectors that define its post locations.
    """

    origin: Optional[PointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    offset_vector: list[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "offsetVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
