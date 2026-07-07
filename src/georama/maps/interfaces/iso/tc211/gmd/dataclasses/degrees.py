from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.degrees_type import DegreesType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Degrees(DegreesType):
    class Meta:
        name = "degrees"
        namespace = "http://www.opengis.net/gml"
