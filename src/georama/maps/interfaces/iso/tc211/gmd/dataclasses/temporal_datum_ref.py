from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    TemporalDatumPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumRef(TemporalDatumPropertyType):
    class Meta:
        name = "temporalDatumRef"
        namespace = "http://www.opengis.net/gml"
