from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.temporal_cstype import (
    TemporalCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCs(TemporalCstype):
    class Meta:
        name = "TemporalCS"
        namespace = "http://www.opengis.net/gml"
