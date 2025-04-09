from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.arc_type import ArcType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CircleType(ArcType):
    pass
