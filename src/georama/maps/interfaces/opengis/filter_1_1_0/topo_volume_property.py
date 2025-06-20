from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topo_volume_property_type import (
    TopoVolumePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolumeProperty(TopoVolumePropertyType):
    class Meta:
        name = "topoVolumeProperty"
        namespace = "http://www.opengis.net/gml"
