from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.conversion_ref_type import (
    ConversionRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConversionRef(ConversionRefType):
    class Meta:
        name = "conversionRef"
        namespace = "http://www.opengis.net/gml"
