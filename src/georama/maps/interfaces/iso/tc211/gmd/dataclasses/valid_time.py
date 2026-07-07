from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_time_primitive_type import (
    TimePrimitivePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValidTime(TimePrimitivePropertyType):
    """
    Gml:validTime is a convenience property element.
    """

    class Meta:
        name = "validTime"
        namespace = "http://www.opengis.net/gml"
