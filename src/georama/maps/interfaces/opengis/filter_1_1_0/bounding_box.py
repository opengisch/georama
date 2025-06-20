from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.envelope_type import EnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundingBox(EnvelopeType):
    """
    A bounding box (or envelope) defining the spatial domain of this object.
    """

    class Meta:
        name = "boundingBox"
        namespace = "http://www.opengis.net/gml"
