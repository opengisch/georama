from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.topo_volume_property_type import (
    TopoVolumePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoVolumeProperty(TopoVolumePropertyType):
    """
    The gml:topoVolumeProperty element may be used in features to express their
    relationship to the referenced topology volume.
    """

    class Meta:
        name = "topoVolumeProperty"
        namespace = "http://www.opengis.net/gml/3.2"
