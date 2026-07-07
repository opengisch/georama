from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.polar_cstype import PolarCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolarCs(PolarCstype):
    class Meta:
        name = "PolarCS"
        namespace = "http://www.opengis.net/gml"
