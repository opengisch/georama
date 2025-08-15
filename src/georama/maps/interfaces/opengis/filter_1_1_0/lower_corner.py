from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.direct_position_type import (
    DirectPositionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LowerCorner(DirectPositionType):
    class Meta:
        global_type = False
