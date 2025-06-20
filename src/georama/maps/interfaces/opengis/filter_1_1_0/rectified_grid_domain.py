from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.rectified_grid_domain_type import (
    RectifiedGridDomainType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridDomain(RectifiedGridDomainType):
    class Meta:
        name = "rectifiedGridDomain"
        namespace = "http://www.opengis.net/gml"
