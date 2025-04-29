from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_parametric_curve_surface_type import (
    AbstractParametricCurveSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractParametricCurveSurface(AbstractParametricCurveSurfaceType):
    """The element provides a substitution group head for the surface patches based
    on parametric curves.

    All properties are specified in the derived subtypes. All derived
    subtypes shall conform to the constraints specified in ISO
    19107:2003, 6.4.40. If provided, the aggregationType attribute shall
    have the value "set".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
