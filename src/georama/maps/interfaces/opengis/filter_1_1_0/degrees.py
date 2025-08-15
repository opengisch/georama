from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.degrees_type import DegreesType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Degrees(DegreesType):
    class Meta:
        name = "degrees"
        namespace = "http://www.opengis.net/gml"
