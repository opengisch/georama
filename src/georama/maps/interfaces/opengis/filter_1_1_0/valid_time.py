from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_primitive_type import (
    TimePrimitivePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValidTime(TimePrimitivePropertyType):
    class Meta:
        name = "validTime"
        namespace = "http://www.opengis.net/gml"
