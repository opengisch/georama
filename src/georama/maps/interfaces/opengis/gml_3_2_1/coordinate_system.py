from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_system_property_type import (
    CoordinateSystemPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateSystem(CoordinateSystemPropertyType):
    """
    An association role to the coordinate system used by this CRS.
    """

    class Meta:
        name = "coordinateSystem"
        namespace = "http://www.opengis.net/gml/3.2"
