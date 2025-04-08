from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.oblique_cartesian_csproperty_type import (
    ObliqueCartesianCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesObliqueCartesianCs(ObliqueCartesianCspropertyType):
    class Meta:
        name = "usesObliqueCartesianCS"
        namespace = "http://www.opengis.net/gml"
