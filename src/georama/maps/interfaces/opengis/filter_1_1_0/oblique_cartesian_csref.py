from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.oblique_cartesian_csref_type import (
    ObliqueCartesianCsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ObliqueCartesianCsref(ObliqueCartesianCsrefType):
    class Meta:
        name = "obliqueCartesianCSRef"
        namespace = "http://www.opengis.net/gml"
