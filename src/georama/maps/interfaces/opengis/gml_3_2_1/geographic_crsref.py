from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.sc_crs_property_type import (
    GeographicCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeographicCrsref(GeographicCrspropertyType):
    class Meta:
        name = "geographicCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
