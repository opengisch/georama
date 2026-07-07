from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.conversion_to_preferred_unit_type import (
    ConversionToPreferredUnitType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConversionToPreferredUnit(ConversionToPreferredUnitType):
    """The elements gml:conversionToPreferredUnit and
    gml:roughConversionToPreferredUnit represent parameters used to convert
    conventional units to preferred units for this physical quantity type.

    A preferred unit is either a Base Unit or a Derived Unit that is
    selected for all values of one physical quantity type.
    """

    class Meta:
        name = "conversionToPreferredUnit"
        namespace = "http://www.opengis.net/gml"
