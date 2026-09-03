from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.unit_of_measure_type import (
    UnitOfMeasureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivationUnitTermType(UnitOfMeasureType):
    exponent: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
