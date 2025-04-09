from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    GeographicCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeographicCrsref(GeographicCrspropertyType):
    class Meta:
        name = "geographicCRSRef"
        namespace = "http://www.opengis.net/gml"
