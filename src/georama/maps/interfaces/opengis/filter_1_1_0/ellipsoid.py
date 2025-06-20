from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoid_type import EllipsoidType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Ellipsoid(EllipsoidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
