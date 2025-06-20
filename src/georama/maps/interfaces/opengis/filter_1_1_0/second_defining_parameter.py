from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.second_defining_parameter_type import (
    SecondDefiningParameterType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SecondDefiningParameter(SecondDefiningParameterType):
    class Meta:
        name = "secondDefiningParameter"
        namespace = "http://www.opengis.net/gml"
