from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.geographic_crstype import (
    GeographicCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeographicCrs(GeographicCrstype):
    class Meta:
        name = "GeographicCRS"
        namespace = "http://www.opengis.net/gml"
