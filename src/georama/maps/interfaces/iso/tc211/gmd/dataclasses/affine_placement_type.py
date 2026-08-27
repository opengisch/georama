from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.direct_position_type import (
    DirectPositionType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AffinePlacementType:
    location: DirectPositionType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    ref_direction: list[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "refDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    in_dimension: int | None = field(
        default=None,
        metadata={
            "name": "inDimension",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    out_dimension: int | None = field(
        default=None,
        metadata={
            "name": "outDimension",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
