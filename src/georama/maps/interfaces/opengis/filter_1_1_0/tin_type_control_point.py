from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.point_property import PointProperty
from georama.maps.interfaces.opengis.filter_1_1_0.pos import Pos
from georama.maps.interfaces.opengis.filter_1_1_0.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TinTypeControlPoint:
    class Meta:
        global_type = False

    pos_list_or_pos_or_point_property: list[PosList | Pos | PointProperty] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "posList",
                    "type": PosList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "pos",
                    "type": Pos,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "pointProperty",
                    "type": PointProperty,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
