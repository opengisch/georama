from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.conversion_to_preferred_unit_type import (
    ConversionToPreferredUnitType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConversionToPreferredUnit(ConversionToPreferredUnitType):
    """
    This element is included when this unit has an accurate conversion to the
    preferred unit for this quantity type.
    """

    class Meta:
        name = "conversionToPreferredUnit"
        namespace = "http://www.opengis.net/gml"
