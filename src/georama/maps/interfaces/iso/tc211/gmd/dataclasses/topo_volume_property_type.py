from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.topo_volume import TopoVolume

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolumePropertyType:
    topo_volume: Optional[TopoVolume] = field(
        default=None,
        metadata={
            "name": "TopoVolume",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
