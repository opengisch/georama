from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    SingleCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SingleCrsref(SingleCrspropertyType):
    class Meta:
        name = "singleCRSRef"
        namespace = "http://www.opengis.net/gml"
