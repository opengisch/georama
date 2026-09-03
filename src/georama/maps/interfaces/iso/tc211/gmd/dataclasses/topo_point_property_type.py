from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.topo_point import TopoPoint

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPointPropertyType:
    topo_point: TopoPoint | None = field(
        default=None,
        metadata={
            "name": "TopoPoint",
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
