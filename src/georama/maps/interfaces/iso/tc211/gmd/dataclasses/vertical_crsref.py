from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vertical_crsproperty_type import (
    VerticalCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCrsref(VerticalCrspropertyType):
    class Meta:
        name = "verticalCRSRef"
        namespace = "http://www.opengis.net/gml"
