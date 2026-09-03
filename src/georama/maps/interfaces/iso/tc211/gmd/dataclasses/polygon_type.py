from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_surface_type import (
    AbstractSurfaceType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.exterior import Exterior
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.interior import Interior

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonType(AbstractSurfaceType):
    exterior: Exterior | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    interior: list[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
