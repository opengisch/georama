from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.temporal_csproperty_type import (
    TemporalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesTemporalCs(TemporalCspropertyType):
    class Meta:
        name = "usesTemporalCS"
        namespace = "http://www.opengis.net/gml"
