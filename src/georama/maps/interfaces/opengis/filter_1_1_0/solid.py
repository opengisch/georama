from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.solid_type import SolidType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Solid(SolidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
