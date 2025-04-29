from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.multi_point_property_type import (
    MultiPointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPosition(MultiPointPropertyType):
    class Meta:
        name = "multiPosition"
        namespace = "http://www.opengis.net/gml/3.2"
