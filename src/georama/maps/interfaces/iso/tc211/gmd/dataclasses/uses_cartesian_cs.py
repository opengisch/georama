from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cartesian_csproperty_type import (
    CartesianCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesCartesianCs(CartesianCspropertyType):
    class Meta:
        name = "usesCartesianCS"
        namespace = "http://www.opengis.net/gml"
