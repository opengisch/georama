from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.multi_point_property_type import (
    MultiPointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCenterOf(MultiPointPropertyType):
    class Meta:
        name = "multiCenterOf"
        namespace = "http://www.opengis.net/gml/3.2"
