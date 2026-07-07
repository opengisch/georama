from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.graph_style_property_type import (
    GraphStylePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GraphStyle2(GraphStylePropertyType):
    class Meta:
        name = "graphStyle"
        namespace = "http://www.opengis.net/gml"
