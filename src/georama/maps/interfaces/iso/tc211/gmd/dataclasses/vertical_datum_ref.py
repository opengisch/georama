from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    VerticalDatumPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumRef(VerticalDatumPropertyType):
    class Meta:
        name = "verticalDatumRef"
        namespace = "http://www.opengis.net/gml"
