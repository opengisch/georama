from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.property_is_like_type import (
    PropertyIsLikeType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsLike(PropertyIsLikeType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
