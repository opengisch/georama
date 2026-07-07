from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.cylinder_type import CylinderType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Cylinder(CylinderType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
