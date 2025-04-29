from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.length_type import LengthType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Distance(LengthType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
