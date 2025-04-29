from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_surface_patch_type import (
    AbstractSurfacePatchType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractParametricCurveSurfaceType(AbstractSurfacePatchType):
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
