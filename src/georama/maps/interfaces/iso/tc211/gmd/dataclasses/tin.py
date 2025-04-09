from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.tin_type import TinType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Tin(TinType):
    """A tin is a triangulated surface that uses the Delauny algorithm or a similar
    algorithm complemented with consideration of stoplines (stopLines), breaklines
    (breakLines), and maximum length of triangle sides (maxLength).

    controlPoint shall contain a set of the positions (three or more)
    used as posts for this TIN (corners of the triangles in the TIN).
    See ISO 19107:2003, 6.4.39 for details.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
