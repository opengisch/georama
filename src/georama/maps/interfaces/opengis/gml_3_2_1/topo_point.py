from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.topo_point_type import TopoPointType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoPoint(TopoPointType):
    """
    The intended use of gml:TopoPoint is to appear within a point feature to
    express the structural and possibly geometric relationships of this feature to
    other features via shared node definitions.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
