from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.temporal_crsref_type import (
    TemporalCrsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCrsref(TemporalCrsrefType):
    class Meta:
        name = "temporalCRSRef"
        namespace = "http://www.opengis.net/gml"
