from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.temporal_csproperty_type import (
    TemporalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesTemporalCs(TemporalCspropertyType):
    class Meta:
        name = "usesTemporalCS"
        namespace = "http://www.opengis.net/gml/3.2"
