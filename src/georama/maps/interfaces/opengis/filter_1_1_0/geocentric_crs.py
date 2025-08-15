from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.geocentric_crstype import (
    GeocentricCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeocentricCrs(GeocentricCrstype):
    class Meta:
        name = "GeocentricCRS"
        namespace = "http://www.opengis.net/gml"
