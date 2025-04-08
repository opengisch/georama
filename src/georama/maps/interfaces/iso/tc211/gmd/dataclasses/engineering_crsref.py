from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.engineering_crsproperty_type import (
    EngineeringCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringCrsref(EngineeringCrspropertyType):
    class Meta:
        name = "engineeringCRSRef"
        namespace = "http://www.opengis.net/gml"
