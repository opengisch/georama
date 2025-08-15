from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topo_point_property_type import (
    TopoPointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPointProperty(TopoPointPropertyType):
    class Meta:
        name = "topoPointProperty"
        namespace = "http://www.opengis.net/gml"
