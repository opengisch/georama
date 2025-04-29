from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.sc_crs_property_type import (
    EngineeringDatumPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EngineeringDatumRef(EngineeringDatumPropertyType):
    class Meta:
        name = "engineeringDatumRef"
        namespace = "http://www.opengis.net/gml/3.2"
