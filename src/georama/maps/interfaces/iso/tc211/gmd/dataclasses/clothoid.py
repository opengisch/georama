from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.clothoid_type import ClothoidType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Clothoid(ClothoidType):
    """A clothoid, or Cornu's spiral, is plane curve whose curvature is a fixed
    function of its length.

    refLocation, startParameter, endParameter and scaleFactor have the
    same meaning as specified in ISO 19107:2003, 6.4.22. interpolation
    is fixed as "clothoid". The content model follows the general
    pattern for the encoding of curve segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
