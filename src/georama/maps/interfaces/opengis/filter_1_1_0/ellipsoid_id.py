from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidId(IdentifierType):
    """
    An identification of an ellipsoid.
    """

    class Meta:
        name = "ellipsoidID"
        namespace = "http://www.opengis.net/gml"
