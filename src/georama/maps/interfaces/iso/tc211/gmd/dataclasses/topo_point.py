from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.topo_point_type import (
    TopoPointType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPoint(TopoPointType):
    """
    The intended use of gml:TopoPoint is to appear within a point feature to
    express the structural and possibly geometric relationships of this feature to
    other features via shared node definitions.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
