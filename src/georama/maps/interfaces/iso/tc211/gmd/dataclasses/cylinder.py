from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cylinder_type import CylinderType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Cylinder(CylinderType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
