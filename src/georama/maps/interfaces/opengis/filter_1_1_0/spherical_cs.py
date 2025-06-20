from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.spherical_cstype import (
    SphericalCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphericalCs(SphericalCstype):
    class Meta:
        name = "SphericalCS"
        namespace = "http://www.opengis.net/gml"
