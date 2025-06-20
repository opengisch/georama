from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.temporal_datum_type import (
    TemporalDatumType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalDatum(TemporalDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
