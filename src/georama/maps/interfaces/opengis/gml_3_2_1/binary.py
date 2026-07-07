from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.binary_type import BinaryType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Binary(BinaryType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
