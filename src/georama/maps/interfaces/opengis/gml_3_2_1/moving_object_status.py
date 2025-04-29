from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.moving_object_status_type import (
    MovingObjectStatusType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MovingObjectStatus(MovingObjectStatusType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
