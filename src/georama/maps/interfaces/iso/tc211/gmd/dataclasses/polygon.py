from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polygon_type import PolygonType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Polygon(PolygonType):
    """A Polygon is a special surface that is defined by a single surface patch
    (see D.3.6).

    The boundary of this patch is coplanar and the polygon uses planar
    interpolation in its interior. The elements exterior and interior
    describe the surface boundary of the polygon.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
