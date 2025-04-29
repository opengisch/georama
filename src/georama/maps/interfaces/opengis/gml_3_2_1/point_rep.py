from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.point_property_type import (
    PointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointRep(PointPropertyType):
    class Meta:
        name = "pointRep"
        namespace = "http://www.opengis.net/gml/3.2"
