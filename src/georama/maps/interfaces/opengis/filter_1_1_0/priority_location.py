from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.priority_location_property_type import (
    PriorityLocationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PriorityLocation(PriorityLocationPropertyType):
    """
    Deprecated in GML 3.1.0.
    """

    class Meta:
        name = "priorityLocation"
        namespace = "http://www.opengis.net/gml"
