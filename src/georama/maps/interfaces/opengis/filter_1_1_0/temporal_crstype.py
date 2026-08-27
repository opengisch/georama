from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_reference_system_type import (
    AbstractReferenceSystemType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_temporal_cs import UsesTemporalCs
from georama.maps.interfaces.opengis.filter_1_1_0.uses_temporal_datum import (
    UsesTemporalDatum,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCrstype(AbstractReferenceSystemType):
    """
    A 1D coordinate reference system used for the recording of time.
    """

    class Meta:
        name = "TemporalCRSType"

    uses_temporal_cs: UsesTemporalCs | None = field(
        default=None,
        metadata={
            "name": "usesTemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    uses_temporal_datum: UsesTemporalDatum | None = field(
        default=None,
        metadata={
            "name": "usesTemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
