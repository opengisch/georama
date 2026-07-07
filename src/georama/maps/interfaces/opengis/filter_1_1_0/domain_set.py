from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.domain_set_type import DomainSetType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DomainSet(DomainSetType):
    class Meta:
        name = "domainSet"
        namespace = "http://www.opengis.net/gml"
