from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.triangulated_surface_type import (
    TriangulatedSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TriangulatedSurface(TriangulatedSurfaceType):
    """A triangulated surface is a polyhedral surface that is composed only of
    triangles.

    There is no restriction on how the triangulation is derived.
    trianglePatches encapsulates the triangles of the triangulated
    surface.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
