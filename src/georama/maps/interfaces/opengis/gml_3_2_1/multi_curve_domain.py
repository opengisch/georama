from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.domain_set_type import DomainSetType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurveDomain(DomainSetType):
    class Meta:
        name = "multiCurveDomain"
        namespace = "http://www.opengis.net/gml/3.2"
