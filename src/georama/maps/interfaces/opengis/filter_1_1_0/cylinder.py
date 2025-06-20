from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.cylinder_type import CylinderType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Cylinder(CylinderType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
