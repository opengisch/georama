from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.reference_system_ref_type import (
    ReferenceSystemRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ReferenceSystemRef(ReferenceSystemRefType):
    class Meta:
        name = "referenceSystemRef"
        namespace = "http://www.opengis.net/gml"
