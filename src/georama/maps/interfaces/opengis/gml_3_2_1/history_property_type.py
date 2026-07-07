from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.moving_object_status import (
    MovingObjectStatus,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class HistoryPropertyType:
    moving_object_status: list[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
