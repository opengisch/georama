from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_surface_domain_type import (
    MultiSurfaceDomainType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceDomain(MultiSurfaceDomainType):
    class Meta:
        name = "multiSurfaceDomain"
        namespace = "http://www.opengis.net/gml"
