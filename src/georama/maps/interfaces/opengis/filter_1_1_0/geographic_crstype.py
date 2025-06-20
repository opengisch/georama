from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_reference_system_type import (
    AbstractReferenceSystemType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_ellipsoidal_cs import (
    UsesEllipsoidalCs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_geodetic_datum import (
    UsesGeodeticDatum,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeographicCrstype(AbstractReferenceSystemType):
    """
    A coordinate reference system based on an ellipsoidal approximation of the
    geoid; this provides an accurate representation of the geometry of geographic
    features for a large portion of the earth's surface.
    """

    class Meta:
        name = "GeographicCRSType"

    uses_ellipsoidal_cs: Optional[UsesEllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "usesEllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
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
