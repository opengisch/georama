from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.priority_location_property_type import (
    PriorityLocationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PriorityLocation(PriorityLocationPropertyType):
    class Meta:
        name = "priorityLocation"
        namespace = "http://www.opengis.net/gml"
