from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topo_volume_type import TopoVolumeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolume(TopoVolumeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
