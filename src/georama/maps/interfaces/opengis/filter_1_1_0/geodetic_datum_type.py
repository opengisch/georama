from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_datum_type import (
    AbstractDatumType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_ellipsoid import UsesEllipsoid
from georama.maps.interfaces.opengis.filter_1_1_0.uses_prime_meridian import (
    UsesPrimeMeridian,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatumType(AbstractDatumType):
    """
    A geodetic datum defines the precise location and orientation in 3-dimensional
    space of a defined ellipsoid (or sphere) that approximates the shape of the
    earth, or of a Cartesian coordinate system centered in this ellipsoid (or
    sphere).
    """

    uses_prime_meridian: Optional[UsesPrimeMeridian] = field(
        default=None,
        metadata={
            "name": "usesPrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    uses_ellipsoid: Optional[UsesEllipsoid] = field(
        default=None,
        metadata={
            "name": "usesEllipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
