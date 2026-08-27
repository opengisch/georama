from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.coordinates import Coordinates
from georama.maps.interfaces.opengis.gml_3_2_1.direct_position_type import (
    DirectPositionType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EnvelopeType:
    lower_corner: DirectPositionType | None = field(
        default=None,
        metadata={
            "name": "lowerCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    upper_corner: DirectPositionType | None = field(
        default=None,
        metadata={
            "name": "upperCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos: list[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "max_occurs": 2,
        },
    )
    coordinates: Coordinates | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    srs_name: str | None = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: int | None = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )
    axis_labels: list[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
            "tokens": True,
        },
    )
    uom_labels: list[str] = field(
        default_factory=list,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
            "tokens": True,
        },
    )
