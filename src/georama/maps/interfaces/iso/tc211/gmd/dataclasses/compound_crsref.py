from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.compound_crsproperty_type import (
    CompoundCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CompoundCrsref(CompoundCrspropertyType):
    class Meta:
        name = "compoundCRSRef"
        namespace = "http://www.opengis.net/gml"
