from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cone_type import ConeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Cone(ConeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
