from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.unit_definition_type import (
    UnitDefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UnitDefinition(UnitDefinitionType):
    """A gml:UnitDefinition is a general definition of a unit of measure.

    This generic element is used only for units for which no
    relationship with other units or units systems is known. The content
    model of gml:UnitDefinition adds three additional properties to
    gml:Definition, gml:quantityType, gml:quantityTypeReference and
    gml:catalogSymbol. The gml:catalogSymbol property optionally gives
    the short symbol used for this unit. This element is usually used
    when the relationship of this unit to other units or units systems
    is unknown.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
