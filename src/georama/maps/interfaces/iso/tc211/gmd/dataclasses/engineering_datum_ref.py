from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    EngineeringDatumPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringDatumRef(EngineeringDatumPropertyType):
    class Meta:
        name = "engineeringDatumRef"
        namespace = "http://www.opengis.net/gml"
