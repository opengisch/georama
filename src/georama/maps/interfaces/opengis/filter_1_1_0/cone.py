from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.cone_type import ConeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Cone(ConeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
