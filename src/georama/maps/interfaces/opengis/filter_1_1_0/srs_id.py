from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SrsId(IdentifierType):
    """
    An identification of a reference system.
    """

    class Meta:
        name = "srsID"
        namespace = "http://www.opengis.net/gml"
