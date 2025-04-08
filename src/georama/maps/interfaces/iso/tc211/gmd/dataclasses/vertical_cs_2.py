from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vertical_csproperty_type import (
    VerticalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCs2(VerticalCspropertyType):
    """
    Gml:verticalCS is an association role to the vertical coordinate system used by
    this CRS.
    """

    class Meta:
        name = "verticalCS"
        namespace = "http://www.opengis.net/gml"
