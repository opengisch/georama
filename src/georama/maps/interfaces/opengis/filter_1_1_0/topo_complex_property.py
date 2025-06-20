from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topo_complex_type import (
    TopoComplexMemberType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoComplexProperty(TopoComplexMemberType):
    class Meta:
        name = "topoComplexProperty"
        namespace = "http://www.opengis.net/gml"
