from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.topo_volume_type import TopoVolumeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoVolume(TopoVolumeType):
    """Gml:TopoVolume represents a homogeneous topological expression, a set of
    directed topologic solids, which if realised are isomorphic to a geometric
    solid primitive.

    The intended use of gml:TopoVolume is to appear within a solid
    feature to express the structural and geometric relationships of
    this solid feature to other features via the shared solid
    definitions.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
