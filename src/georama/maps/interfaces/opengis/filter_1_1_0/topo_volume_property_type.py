from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.topo_volume import TopoVolume

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolumePropertyType:
    topo_volume: TopoVolume | None = field(
        default=None,
        metadata={
            "name": "TopoVolume",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
