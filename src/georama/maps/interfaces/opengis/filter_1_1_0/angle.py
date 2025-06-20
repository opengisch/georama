from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Angle(MeasureType):
    class Meta:
        name = "angle"
        namespace = "http://www.opengis.net/gml"
