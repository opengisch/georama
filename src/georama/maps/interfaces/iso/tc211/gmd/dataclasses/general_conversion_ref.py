from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    GeneralConversionPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralConversionRef(GeneralConversionPropertyType):
    class Meta:
        name = "generalConversionRef"
        namespace = "http://www.opengis.net/gml"
