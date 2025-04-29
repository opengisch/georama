from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.spherical_csproperty_type import (
    SphericalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SphericalCsref(SphericalCspropertyType):
    class Meta:
        name = "sphericalCSRef"
        namespace = "http://www.opengis.net/gml/3.2"
