from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.conversion_property_type import (
    ConversionPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConversionRef(ConversionPropertyType):
    class Meta:
        name = "conversionRef"
        namespace = "http://www.opengis.net/gml"
