from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.conventional_unit_type import (
    ConventionalUnitType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConventionalUnit(ConventionalUnitType):
    """Conventional units that are neither base units nor defined by direct
    combination of base units are used in many application domains.

    For example electronVolt for energy, feet and nautical miles for
    length.  In most cases there is a known, usually linear, conversion
    to a preferred unit which is either a base unit or derived by direct
    combination of base units. The gml:ConventionalUnit extends
    gml:UnitDefinition with a property that describes a conversion to a
    preferred unit for this physical quantity.  When the conversion is
    exact, the element gml:conversionToPreferredUnit should be used, or
    when the conversion is not exact the element
    gml:roughConversionToPreferredUnit is available. Both of these
    elements have the same content model.  The gml:derivationUnitTerm
    property defined above is included to allow a user to optionally
    record how this unit may be derived from other (“more primitive”)
    units.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
