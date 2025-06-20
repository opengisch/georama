from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.formula_type import FormulaType
from georama.maps.interfaces.opengis.filter_1_1_0.unit_of_measure_type import (
    UnitOfMeasureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConversionToPreferredUnitType(UnitOfMeasureType):
    """Relation of a unit to the preferred unit for this quantity type, specified
    by an arithmetic conversion (scaling and/or offset).

    A preferred unit is either a base unit or a derived unit selected
    for all units of one quantity type. The mandatory attribute "uom"
    shall reference the preferred unit that this conversion applies to.
    The conversion is specified by one of two alternative elements:
    "factor" or "formula".

    :ivar factor: Specification of the scale factor by which a value
        using this unit of measure can be multiplied to obtain the
        corresponding value using the preferred unit of measure.
    :ivar formula: Specification of the formula by which a value using
        this unit of measure can be converted to obtain the
        corresponding value using the preferred unit of measure.
    """

    factor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    formula: Optional[FormulaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
