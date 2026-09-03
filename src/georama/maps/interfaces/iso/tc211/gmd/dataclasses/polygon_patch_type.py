from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_surface_patch_type import (
    AbstractSurfacePatchType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.exterior import Exterior
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.interior import Interior
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_interpolation_type import (
    SurfaceInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatchType(AbstractSurfacePatchType):
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
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        },
    )
