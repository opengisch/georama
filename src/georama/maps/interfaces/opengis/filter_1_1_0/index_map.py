from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.index_map_type import IndexMapType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IndexMap(IndexMapType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
