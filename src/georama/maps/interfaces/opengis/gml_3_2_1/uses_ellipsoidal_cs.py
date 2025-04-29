from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.ellipsoidal_csproperty_type import (
    EllipsoidalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesEllipsoidalCs(EllipsoidalCspropertyType):
    class Meta:
        name = "usesEllipsoidalCS"
        namespace = "http://www.opengis.net/gml/3.2"
