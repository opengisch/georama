from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.temporal_crsproperty_type import (
    TemporalCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalCrsref(TemporalCrspropertyType):
    class Meta:
        name = "temporalCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
