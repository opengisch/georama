from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_primitive_type import (
    TimePrimitivePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ValidTime(TimePrimitivePropertyType):
    """
    Gml:validTime is a convenience property element.
    """

    class Meta:
        name = "validTime"
        namespace = "http://www.opengis.net/gml/3.2"
