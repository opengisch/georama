from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.ellipsoid_property_type import (
    EllipsoidPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Ellipsoid2(EllipsoidPropertyType):
    """
    Gml:ellipsoid is an association role to the ellipsoid used by this geodetic
    datum.
    """

    class Meta:
        name = "ellipsoid"
        namespace = "http://www.opengis.net/gml/3.2"
