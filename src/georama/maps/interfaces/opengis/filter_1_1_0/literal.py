from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.literal_type import LiteralType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Literal(LiteralType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
