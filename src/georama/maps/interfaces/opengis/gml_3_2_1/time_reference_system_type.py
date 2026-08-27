from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeReferenceSystemType(DefinitionType):
    domain_of_validity: str | None = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
