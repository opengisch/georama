from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.arc_by_center_point_type import (
    ArcByCenterPointType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcByCenterPoint(ArcByCenterPointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
