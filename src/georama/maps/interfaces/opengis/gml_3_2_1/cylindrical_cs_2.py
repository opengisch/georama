from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.cylindrical_csproperty_type import (
    CylindricalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CylindricalCs2(CylindricalCspropertyType):
    """
    Gml:cylindricalCS is an association role to the cylindrical coordinate system
    used by this CRS.
    """

    class Meta:
        name = "cylindricalCS"
        namespace = "http://www.opengis.net/gml/3.2"
