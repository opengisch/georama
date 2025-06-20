from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.engineering_datum_ref_type import (
    EngineeringDatumRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringDatumRef(EngineeringDatumRefType):
    class Meta:
        name = "engineeringDatumRef"
        namespace = "http://www.opengis.net/gml"
