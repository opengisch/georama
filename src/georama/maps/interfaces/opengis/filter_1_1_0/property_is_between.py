from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.property_is_between_type import (
    PropertyIsBetweenType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsBetween(PropertyIsBetweenType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
