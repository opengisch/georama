from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.projected_crsref_type import (
    ProjectedCrsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ProjectedCrsref(ProjectedCrsrefType):
    class Meta:
        name = "projectedCRSRef"
        namespace = "http://www.opengis.net/gml"
