from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MethodId(IdentifierType):
    """
    An identification of an operation method.
    """

    class Meta:
        name = "methodID"
        namespace = "http://www.opengis.net/gml"
