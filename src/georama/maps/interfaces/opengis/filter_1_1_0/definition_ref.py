from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionRef(ReferenceType):
    class Meta:
        name = "definitionRef"
        namespace = "http://www.opengis.net/gml"
