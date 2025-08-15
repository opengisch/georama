from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.engineering_datum_type import (
    EngineeringDatumType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringDatum(EngineeringDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
