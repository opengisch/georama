from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.surface_type import SurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TriangulatedSurface(SurfaceType):
    """A triangulated surface is a polyhedral surface that is composed only of
    triangles.

    There is no restriction on how the triangulation is derived.
    trianglePatches encapsulates the triangles of the triangulated
    surface.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
