from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.projected_crsproperty_type import (
    ProjectedCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ProjectedCrsref(ProjectedCrspropertyType):
    class Meta:
        name = "projectedCRSRef"
        namespace = "http://www.opengis.net/gml"
