from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_reference_system_type import (
    AbstractReferenceSystemType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_cartesian_cs import (
    UsesCartesianCs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_geodetic_datum import (
    UsesGeodeticDatum,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_spherical_cs import (
    UsesSphericalCs,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeocentricCrstype(AbstractReferenceSystemType):
    """A 3D coordinate reference system with the origin at the approximate centre
    of mass of the earth.

    A geocentric CRS deals with the earth's curvature by taking a 3D
    spatial view, which obviates the need to model the earth's
    curvature.
    """

    class Meta:
        name = "GeocentricCRSType"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    uses_spherical_cs: Optional[UsesSphericalCs] = field(
        default=None,
        metadata={
            "name": "usesSphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
