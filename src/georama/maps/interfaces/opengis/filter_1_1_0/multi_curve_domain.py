from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_curve_domain_type import (
    MultiCurveDomainType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCurveDomain(MultiCurveDomainType):
    class Meta:
        name = "multiCurveDomain"
        namespace = "http://www.opengis.net/gml"
