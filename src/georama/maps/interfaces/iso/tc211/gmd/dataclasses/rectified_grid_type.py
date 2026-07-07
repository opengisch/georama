from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.grid_type import GridType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_property_type import (
    PointPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridType(GridType):
    origin: Optional[PointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    offset_vector: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "offsetVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
