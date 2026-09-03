from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.topo_volume import TopoVolume

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoVolumePropertyType:
    topo_volume: TopoVolume | None = field(
        default=None,
        metadata={
            "name": "TopoVolume",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
