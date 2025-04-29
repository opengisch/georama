from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.sc_crs_property_type import (
    SingleCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SingleCrsref(SingleCrspropertyType):
    class Meta:
        name = "singleCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
