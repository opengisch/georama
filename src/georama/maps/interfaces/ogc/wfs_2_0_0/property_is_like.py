from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_like_type import (
    PropertyIsLikeType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsLike(PropertyIsLikeType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
