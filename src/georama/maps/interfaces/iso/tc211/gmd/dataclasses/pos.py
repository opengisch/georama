from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.direct_position_type import (
    DirectPositionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Pos(DirectPositionType):
    class Meta:
        name = "pos"
        namespace = "http://www.opengis.net/gml"
