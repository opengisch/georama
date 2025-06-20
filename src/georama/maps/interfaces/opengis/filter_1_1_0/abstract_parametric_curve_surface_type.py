from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_surface_patch_type import (
    AbstractSurfacePatchType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractParametricCurveSurfaceType(AbstractSurfacePatchType):
    pass
