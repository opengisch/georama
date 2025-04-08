from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.prime_meridian_property_type import (
    PrimeMeridianPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesPrimeMeridian(PrimeMeridianPropertyType):
    class Meta:
        name = "usesPrimeMeridian"
        namespace = "http://www.opengis.net/gml"
