from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.linear_cstype import LinearCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearCs(LinearCstype):
    class Meta:
        name = "LinearCS"
        namespace = "http://www.opengis.net/gml"
