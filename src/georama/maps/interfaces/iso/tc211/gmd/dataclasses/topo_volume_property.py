from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.topo_volume_property_type import (
    TopoVolumePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolumeProperty(TopoVolumePropertyType):
    """
    The gml:topoVolumeProperty element may be used in features to express their
    relationship to the referenced topology volume.
    """

    class Meta:
        name = "topoVolumeProperty"
        namespace = "http://www.opengis.net/gml"
