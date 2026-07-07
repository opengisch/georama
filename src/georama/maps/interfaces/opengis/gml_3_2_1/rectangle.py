from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.rectangle_type import RectangleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Rectangle(RectangleType):
    """Gml:Rectangle represents a rectangle as a surface patch with an outer
    boundary consisting of a linear ring.

    Note that this is a polygon (subtype) with no inner boundaries. The
    number of points in the linear ring shall be five. The ring (element
    exterior) shall be a gml:LinearRing and shall form a rectangle; the
    first and the last position shall be coincident. interpolation is
    fixed to "planar", i.e. an interpolation shall return points on a
    single plane. The boundary of the patch shall be contained within
    that plane.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
