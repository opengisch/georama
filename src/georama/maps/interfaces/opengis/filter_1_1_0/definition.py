from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Definition(DefinitionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
