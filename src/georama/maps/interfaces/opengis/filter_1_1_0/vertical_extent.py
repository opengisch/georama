from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.envelope_type import EnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalExtent(EnvelopeType):
    """
    An interval defining the vertical spatial domain of this object.
    """

    class Meta:
        name = "verticalExtent"
        namespace = "http://www.opengis.net/gml"
