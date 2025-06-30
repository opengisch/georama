from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_null_type import (
    PropertyIsNullType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsNull(PropertyIsNullType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
