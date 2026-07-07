from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.envelope_type import EnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Envelope(EnvelopeType):
    """Envelope defines an extent using a pair of positions defining opposite
    corners in arbitrary dimensions.

    The first direct position is the "lower corner" (a coordinate
    position consisting of all the minimal ordinates for each dimension
    for all points within the envelope), the second one the "upper
    corner" (a coordinate position consisting of all the maximal
    ordinates for each dimension for all points within the envelope).
    The use of the properties “coordinates” and “pos” has been
    deprecated. The explicitly named properties “lowerCorner” and
    “upperCorner” shall be used instead.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
