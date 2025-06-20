from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_point_property_type import (
    MultiPointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCenterOf(MultiPointPropertyType):
    class Meta:
        name = "multiCenterOf"
        namespace = "http://www.opengis.net/gml"
