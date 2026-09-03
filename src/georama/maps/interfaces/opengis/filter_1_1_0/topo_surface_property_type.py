from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.topo_surface import TopoSurface

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoSurfacePropertyType:
    topo_surface: TopoSurface | None = field(
        default=None,
        metadata={
            "name": "TopoSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
