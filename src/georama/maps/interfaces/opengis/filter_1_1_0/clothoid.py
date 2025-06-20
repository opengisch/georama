from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.clothoid_type import ClothoidType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Clothoid(ClothoidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
