from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_solid_type import MultiSolidType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolid(MultiSolidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
