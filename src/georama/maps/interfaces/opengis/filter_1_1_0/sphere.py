from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.sphere_type import SphereType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Sphere(SphereType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
