from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.arc_by_center_point_type import (
    ArcByCenterPointType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CircleByCenterPointType(ArcByCenterPointType):
    start_angle: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    end_angle: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
