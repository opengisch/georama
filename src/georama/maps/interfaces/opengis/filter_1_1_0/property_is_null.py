from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.property_is_null_type import (
    PropertyIsNullType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsNull(PropertyIsNullType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
