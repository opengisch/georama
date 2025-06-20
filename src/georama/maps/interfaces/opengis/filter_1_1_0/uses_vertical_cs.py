from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.vertical_csref_type import (
    VerticalCsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesVerticalCs(VerticalCsrefType):
    """
    Association to the vertical coordinate system used by this CRS.
    """

    class Meta:
        name = "usesVerticalCS"
        namespace = "http://www.opengis.net/gml"
