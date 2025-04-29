from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.base_unit_type import BaseUnitType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BaseUnit(BaseUnitType):
    """A base unit is a unit of measure that cannot be derived by combination of
    other base units within a particular system of units.

    For example, in the SI system of units, the base units are metre,
    kilogram, second, Ampere, Kelvin, mole, and candela, for the
    physical quantity types length, mass, time interval, electric
    current, thermodynamic temperature, amount of substance and luminous
    intensity, respectively. gml:BaseUnit extends generic
    gml:UnitDefinition with the property gml:unitsSystem, which carries
    a reference to the units system to which this base unit is asserted
    to belong.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
