from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.geocentric_crsref_type import (
    GeocentricCrsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeocentricCrsref(GeocentricCrsrefType):
    class Meta:
        name = "geocentricCRSRef"
        namespace = "http://www.opengis.net/gml"
