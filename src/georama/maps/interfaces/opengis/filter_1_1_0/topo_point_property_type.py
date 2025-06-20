from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.topo_point import TopoPoint

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPointPropertyType:
    topo_point: Optional[TopoPoint] = field(
        default=None,
        metadata={
            "name": "TopoPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
