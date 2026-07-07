from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.topo_complex_type import (
    TopoComplexMemberType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoComplexProperty(TopoComplexMemberType):
    """
    The gml:topoComplexProperty property element encodes the relationship between a
    GML object and a topological complex.
    """

    class Meta:
        name = "topoComplexProperty"
        namespace = "http://www.opengis.net/gml"
