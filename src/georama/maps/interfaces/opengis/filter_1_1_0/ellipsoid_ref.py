from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoid_ref_type import (
    EllipsoidRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidRef(EllipsoidRefType):
    class Meta:
        name = "ellipsoidRef"
        namespace = "http://www.opengis.net/gml"
