from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.direct_position_list_type import (
    DirectPositionListType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PosList(DirectPositionListType):
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml"
