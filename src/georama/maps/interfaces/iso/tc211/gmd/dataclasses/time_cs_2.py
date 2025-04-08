from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_csproperty_type import (
    TimeCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCs2(TimeCspropertyType):
    """
    Gml:timeCS is an association role to the time coordinate system used by this
    CRS.
    """

    class Meta:
        name = "timeCS"
        namespace = "http://www.opengis.net/gml"
