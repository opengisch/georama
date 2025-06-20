from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.compound_crsref_type import (
    CompoundCrsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CompoundCrsref(CompoundCrsrefType):
    class Meta:
        name = "compoundCRSRef"
        namespace = "http://www.opengis.net/gml"
