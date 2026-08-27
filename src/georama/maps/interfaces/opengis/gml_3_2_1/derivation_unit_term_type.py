from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.unit_of_measure_type import (
    UnitOfMeasureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivationUnitTermType(UnitOfMeasureType):
    exponent: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
