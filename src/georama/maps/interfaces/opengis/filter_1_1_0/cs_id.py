from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CsId(IdentifierType):
    """
    An identification of a coordinate system.
    """

    class Meta:
        name = "csID"
        namespace = "http://www.opengis.net/gml"
