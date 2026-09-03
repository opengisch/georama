from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_reference_system_type import (
    AbstractReferenceSystemType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_vertical_cs import UsesVerticalCs
from georama.maps.interfaces.opengis.filter_1_1_0.uses_vertical_datum import (
    UsesVerticalDatum,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCrstype(AbstractReferenceSystemType):
    """A 1D coordinate reference system used for recording heights or depths.

    Vertical CRSs make use of the direction of gravity to define the
    concept of height or depth, but the relationship with gravity may
    not be straightforward. By implication, ellipsoidal heights (h)
    cannot be captured in a vertical coordinate reference system.
    Ellipsoidal heights cannot exist independently, but only as an
    inseparable part of a 3D coordinate tuple defined in a geographic 3D
    coordinate reference system.
    """

    class Meta:
        name = "VerticalCRSType"

    uses_vertical_cs: UsesVerticalCs | None = field(
        default=None,
        metadata={
            "name": "usesVerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    uses_vertical_datum: UsesVerticalDatum | None = field(
        default=None,
        metadata={
            "name": "usesVerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
