from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_surface_patch_type import (
    AbstractSurfacePatchType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractSurfacePatch(AbstractSurfacePatchType):
    """A surface patch defines a homogenuous portion of a surface.

    The AbstractSurfacePatch element is the abstract head of the
    substituition group for all surface patch elements describing a
    continuous portion of a surface. All surface patches shall have an
    attribute interpolation (declared in the types derived from
    gml:AbstractSurfacePatchType) specifying the interpolation mechanism
    used for the patch using gml:SurfaceInterpolationType.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
