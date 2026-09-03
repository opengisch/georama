from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.topo_surface import TopoSurface

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoSurfacePropertyType:
    topo_surface: TopoSurface | None = field(
        default=None,
        metadata={
            "name": "TopoSurface",
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
