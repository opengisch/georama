from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.derived_crsproperty_type import (
    DerivedCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedCrsref(DerivedCrspropertyType):
    class Meta:
        name = "derivedCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
