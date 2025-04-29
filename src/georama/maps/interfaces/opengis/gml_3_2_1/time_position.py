from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.time_position_type import (
    TimePositionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimePosition(TimePositionType):
    """
    This element is used directly as a property of gml:TimeInstant (see 15.2.2.3),
    and may also be used in application schemas.
    """

    class Meta:
        name = "timePosition"
        namespace = "http://www.opengis.net/gml/3.2"
