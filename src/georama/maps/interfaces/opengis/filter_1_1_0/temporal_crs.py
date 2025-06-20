from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.temporal_crstype import (
    TemporalCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCrs(TemporalCrstype):
    class Meta:
        name = "TemporalCRS"
        namespace = "http://www.opengis.net/gml"
