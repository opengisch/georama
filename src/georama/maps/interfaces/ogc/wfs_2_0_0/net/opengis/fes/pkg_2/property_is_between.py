from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_between_type import (
    PropertyIsBetweenType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsBetween(PropertyIsBetweenType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
