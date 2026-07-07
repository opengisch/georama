from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.formula_type import FormulaType
from georama.maps.interfaces.opengis.gml_3_2_1.unit_of_measure_type import (
    UnitOfMeasureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ConversionToPreferredUnitType(UnitOfMeasureType):
    """The inherited attribute uom references the preferred unit that this
    conversion applies to. The conversion of a unit to the preferred unit for this
    physical quantity type is specified by an arithmetic conversion (scaling and/or
    offset). The content model extends gml:UnitOfMeasureType, which has a mandatory
    attribute uom which identifies the preferred unit for the physical quantity
    type that this conversion applies to. The conversion is specified by a choice
    of.

    -       gml:factor, which defines the scale factor, or
    -       gml:formula, which defines a formula
    by which a value using the conventional unit of measure can be converted to obtain the corresponding value using the preferred unit of measure.
    The formula defines the parameters of a simple formula by which a value using the conventional unit of measure can be converted to the corresponding value using the preferred unit of measure. The formula element contains elements a, b, c and d, whose values use the XML Schema type double. These values are used in the formula y = (a + bx) / (c + dx), where x is a value using this unit, and y is the corresponding value using the base unit. The elements a and d are optional, and if values are not provided, those parameters are considered to be zero. If values are not provided for both a and d, the formula is equivalent to a fraction with numerator and denominator parameters.
    """

    factor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    formula: Optional[FormulaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
