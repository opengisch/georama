from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.unit_of_measure_type import (
    UnitOfMeasureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivationUnitTermType(UnitOfMeasureType):
    """Definition of one unit term for a derived unit of measure.

    This unit term references another unit of measure (uom) and provides
    an integer exponent applied to that unit in defining the compound
    unit. The exponent can be positive or negative, but not zero.
    """

    exponent: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
