from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParameterId(IdentifierType):
    """
    An identification of an operation parameter.
    """

    class Meta:
        name = "parameterID"
        namespace = "http://www.opengis.net/gml"
