from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.inverse_flattening import (
    InverseFlattening,
)
from georama.maps.interfaces.opengis.filter_1_1_0.is_sphere import IsSphere
from georama.maps.interfaces.opengis.filter_1_1_0.semi_minor_axis import SemiMinorAxis

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SecondDefiningParameterType:
    """Definition of the second parameter that defines the shape of an ellipsoid.

    An ellipsoid requires two defining parameters: semi-major axis and inverse flattening or semi-major axis and semi-minor axis. When the reference body is a sphere rather than an ellipsoid, only a single defining parameter is required, namely the radius of the sphere; in that case, the semi-major axis "degenerates" into the radius of the sphere.
    """

    inverse_flattening_or_semi_minor_axis_or_is_sphere: Optional[
        Union[InverseFlattening, SemiMinorAxis, IsSphere]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "inverseFlattening",
                    "type": InverseFlattening,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "semiMinorAxis",
                    "type": SemiMinorAxis,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "isSphere",
                    "type": IsSphere,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
