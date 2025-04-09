from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.derived_crsproperty_type import (
    DerivedCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedCrsref(DerivedCrspropertyType):
    class Meta:
        name = "derivedCRSRef"
        namespace = "http://www.opengis.net/gml"
