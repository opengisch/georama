from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.compound_crsproperty_type import (
    CompoundCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CompoundCrsref(CompoundCrspropertyType):
    class Meta:
        name = "compoundCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
