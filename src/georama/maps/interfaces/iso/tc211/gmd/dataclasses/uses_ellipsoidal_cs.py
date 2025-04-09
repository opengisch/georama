from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ellipsoidal_csproperty_type import (
    EllipsoidalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesEllipsoidalCs(EllipsoidalCspropertyType):
    class Meta:
        name = "usesEllipsoidalCS"
        namespace = "http://www.opengis.net/gml"
