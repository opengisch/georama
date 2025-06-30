from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.angle_type import AngleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class HorizontalAngle(AngleType):
    class Meta:
        global_type = False
