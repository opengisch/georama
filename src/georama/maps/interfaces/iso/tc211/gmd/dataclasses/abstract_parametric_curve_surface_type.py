from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_surface_patch_type import (
    AbstractSurfacePatchType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.aggregation_type import (
    AggregationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractParametricCurveSurfaceType(AbstractSurfacePatchType):
    aggregation_type: AggregationType | None = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
