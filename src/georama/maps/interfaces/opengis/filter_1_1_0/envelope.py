from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.envelope_type import EnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Envelope(EnvelopeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
