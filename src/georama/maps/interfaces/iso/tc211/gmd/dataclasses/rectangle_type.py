from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_surface_patch_type import (
    AbstractSurfacePatchType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.exterior import Exterior
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_interpolation_type import (
    SurfaceInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectangleType(AbstractSurfacePatchType):
    exterior: Exterior | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        },
    )
