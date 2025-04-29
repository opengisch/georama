from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.multi_geometry_property_type import (
    MultiGeometryPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiGeometryProperty(MultiGeometryPropertyType):
    class Meta:
        name = "multiGeometryProperty"
        namespace = "http://www.opengis.net/gml/3.2"
