from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.moving_object_status_type import (
    MovingObjectStatusType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MovingObjectStatus(MovingObjectStatusType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
