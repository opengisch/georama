from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.time_csproperty_type import (
    TimeCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesTimeCs(TimeCspropertyType):
    class Meta:
        name = "usesTimeCS"
        namespace = "http://www.opengis.net/gml/3.2"
