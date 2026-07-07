from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.geocentric_crsproperty_type import (
    GeocentricCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeocentricCrsref(GeocentricCrspropertyType):
    class Meta:
        name = "geocentricCRSRef"
        namespace = "http://www.opengis.net/gml"
