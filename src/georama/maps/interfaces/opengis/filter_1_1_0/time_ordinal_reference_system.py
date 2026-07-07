from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.time_ordinal_reference_system_type import (
    TimeOrdinalReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalReferenceSystem(TimeOrdinalReferenceSystemType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
