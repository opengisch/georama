from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.oblique_cartesian_csproperty_type import (
    ObliqueCartesianCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesObliqueCartesianCs(ObliqueCartesianCspropertyType):
    class Meta:
        name = "usesObliqueCartesianCS"
        namespace = "http://www.opengis.net/gml/3.2"
