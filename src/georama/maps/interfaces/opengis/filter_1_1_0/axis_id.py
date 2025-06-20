from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AxisId(IdentifierType):
    """
    An identification of a coordinate system axis.
    """

    class Meta:
        name = "axisID"
        namespace = "http://www.opengis.net/gml"
