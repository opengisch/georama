from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.prime_meridian_property_type import (
    PrimeMeridianPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesPrimeMeridian(PrimeMeridianPropertyType):
    class Meta:
        name = "usesPrimeMeridian"
        namespace = "http://www.opengis.net/gml/3.2"
