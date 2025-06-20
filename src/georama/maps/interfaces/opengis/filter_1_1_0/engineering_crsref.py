from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.engineering_crsref_type import (
    EngineeringCrsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringCrsref(EngineeringCrsrefType):
    class Meta:
        name = "engineeringCRSRef"
        namespace = "http://www.opengis.net/gml"
