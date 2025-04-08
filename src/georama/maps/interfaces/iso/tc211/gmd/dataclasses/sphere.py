from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sphere_type import SphereType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Sphere(SphereType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
