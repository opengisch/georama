from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.scale_type import ScaleType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Scale(ScaleType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
