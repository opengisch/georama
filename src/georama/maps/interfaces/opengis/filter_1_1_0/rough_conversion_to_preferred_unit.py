from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.conversion_to_preferred_unit_type import (
    ConversionToPreferredUnitType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RoughConversionToPreferredUnit(ConversionToPreferredUnitType):
    """
    This element is included when the correct definition of this unit is unknown,
    but this unit has a rough or inaccurate conversion to the preferred unit for
    this quantity type.
    """

    class Meta:
        name = "roughConversionToPreferredUnit"
        namespace = "http://www.opengis.net/gml"
