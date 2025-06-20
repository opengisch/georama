from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.property_name_type import (
    PropertyNameType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyName(PropertyNameType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
