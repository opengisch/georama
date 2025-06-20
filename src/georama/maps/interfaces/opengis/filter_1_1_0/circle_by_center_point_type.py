from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.arc_by_center_point_type import (
    ArcByCenterPointType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CircleByCenterPointType(ArcByCenterPointType):
    """A CircleByCenterPoint is an ArcByCenterPoint with identical start and end
    angle to form a full circle.

    Again, this represenation can be used only in 2D.
    """
