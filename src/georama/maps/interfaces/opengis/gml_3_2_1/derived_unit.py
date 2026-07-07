from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.derived_unit_type import DerivedUnitType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedUnit(DerivedUnitType):
    """Derived units are defined by combination of other units.

    Derived units are used for quantities other than those corresponding
    to the base units, such as hertz (s-1) for frequency, Newton
    (kg.m/s2) for force.  Derived units based directly on base units are
    usually preferred for quantities other than the fundamental
    quantities within a system. If a derived unit is not the preferred
    unit, the gml:ConventionalUnit element should be used instead. The
    gml:DerivedUnit extends gml:UnitDefinition with the property
    gml:derivationUnitTerms.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
