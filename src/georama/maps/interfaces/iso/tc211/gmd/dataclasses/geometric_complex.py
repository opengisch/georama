from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.geometric_complex_type import (
    GeometricComplexType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometricComplex(GeometricComplexType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
