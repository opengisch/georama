from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.temporal_datum_ref_type import (
    TemporalDatumRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumRef(TemporalDatumRefType):
    class Meta:
        name = "temporalDatumRef"
        namespace = "http://www.opengis.net/gml"
