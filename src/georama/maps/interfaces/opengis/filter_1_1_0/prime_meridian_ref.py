from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.prime_meridian_ref_type import (
    PrimeMeridianRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridianRef(PrimeMeridianRefType):
    class Meta:
        name = "primeMeridianRef"
        namespace = "http://www.opengis.net/gml"
