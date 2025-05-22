from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_crstype import (
    GeneralConversionPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeneralConversionRef(GeneralConversionPropertyType):
    class Meta:
        name = "generalConversionRef"
        namespace = "http://www.opengis.net/gml/3.2"
