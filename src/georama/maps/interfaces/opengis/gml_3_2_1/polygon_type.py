from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_surface_type import (
    AbstractSurfaceType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.exterior import Exterior
from georama.maps.interfaces.opengis.gml_3_2_1.interior import Interior

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PolygonType(AbstractSurfaceType):
    exterior: Exterior | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interior: list[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
