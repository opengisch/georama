from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.topo_point import TopoPoint

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoPointPropertyType:
    topo_point: Optional[TopoPoint] = field(
        default=None,
        metadata={
            "name": "TopoPoint",
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
