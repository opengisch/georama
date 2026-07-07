from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.temporal_cstype import TemporalCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCs(TemporalCstype):
    class Meta:
        name = "TemporalCS"
        namespace = "http://www.opengis.net/gml"
