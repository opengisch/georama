from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.geometric_complex_type import (
    GeometricComplexType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometricComplex(GeometricComplexType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
