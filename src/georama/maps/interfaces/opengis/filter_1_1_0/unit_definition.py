from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.unit_definition_type import (
    UnitDefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UnitDefinition(UnitDefinitionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
