from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    AbstractGeneralConversionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralConversion(AbstractGeneralConversionType):
    class Meta:
        name = "_GeneralConversion"
        namespace = "http://www.opengis.net/gml"
