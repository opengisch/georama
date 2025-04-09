from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vertical_csproperty_type import (
    VerticalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesVerticalCs(VerticalCspropertyType):
    class Meta:
        name = "usesVerticalCS"
        namespace = "http://www.opengis.net/gml"
