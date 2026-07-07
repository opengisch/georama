from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    GeneralConversionRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralConversionRef(GeneralConversionRefType):
    class Meta:
        name = "generalConversionRef"
        namespace = "http://www.opengis.net/gml"
