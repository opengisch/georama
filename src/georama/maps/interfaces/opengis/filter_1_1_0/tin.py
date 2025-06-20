from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.tin_type import TinType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Tin(TinType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
