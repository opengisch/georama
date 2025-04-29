from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.coordinates import Coordinates
from georama.maps.interfaces.opengis.gml_3_2_1.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointType(AbstractGeometricPrimitiveType):
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
