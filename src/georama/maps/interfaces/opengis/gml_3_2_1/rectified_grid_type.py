from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.grid_type import GridType
from georama.maps.interfaces.opengis.gml_3_2_1.point_property_type import (
    PointPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class RectifiedGridType(GridType):
    origin: PointPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    offset_vector: list[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "offsetVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
