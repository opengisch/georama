from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ring_type import RingType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Ring(RingType):
    """A ring is used to represent a single connected component of a surface
    boundary as specified in ISO 19107:2003, 6.3.6.

    Every gml:curveMember references or contains one curve, i.e. any
    element which is substitutable for gml:AbstractCurve. In the context
    of a ring, the curves describe the boundary of the surface. The
    sequence of curves shall be contiguous and connected in a cycle. If
    provided, the aggregationType attribute shall have the value
    “sequence”.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
