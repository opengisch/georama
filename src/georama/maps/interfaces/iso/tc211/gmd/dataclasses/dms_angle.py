from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dmsangle_type import DmsangleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DmsAngle(DmsangleType):
    class Meta:
        name = "dmsAngle"
        namespace = "http://www.opengis.net/gml"
