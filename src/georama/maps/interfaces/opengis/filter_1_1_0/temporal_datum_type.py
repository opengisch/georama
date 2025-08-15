from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.origin import Origin
from georama.maps.interfaces.opengis.filter_1_1_0.temporal_datum_base_type import (
    TemporalDatumBaseType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumType(TemporalDatumBaseType):
    """Defines the origin of a temporal coordinate reference system.

    This type extends the TemporalDatumRestrictionType to add the
    "origin" element with the dateTime type.
    """

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
