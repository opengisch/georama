from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.grid_domain_type import GridDomainType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridDomain(GridDomainType):
    class Meta:
        name = "gridDomain"
        namespace = "http://www.opengis.net/gml"
