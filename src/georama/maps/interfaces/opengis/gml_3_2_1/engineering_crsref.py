from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.engineering_crsproperty_type import (
    EngineeringCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EngineeringCrsref(EngineeringCrspropertyType):
    class Meta:
        name = "engineeringCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
