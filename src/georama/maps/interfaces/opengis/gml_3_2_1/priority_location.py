from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.priority_location_property_type import (
    PriorityLocationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PriorityLocation(PriorityLocationPropertyType):
    class Meta:
        name = "priorityLocation"
        namespace = "http://www.opengis.net/gml/3.2"
