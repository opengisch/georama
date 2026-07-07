from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_point_type import MultiPointType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPoint(MultiPointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
