from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    GeodeticDatumPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatumRef(GeodeticDatumPropertyType):
    class Meta:
        name = "geodeticDatumRef"
        namespace = "http://www.opengis.net/gml"
