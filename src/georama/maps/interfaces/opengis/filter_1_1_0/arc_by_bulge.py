from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.arc_by_bulge_type import (
    ArcByBulgeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcByBulge(ArcByBulgeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
