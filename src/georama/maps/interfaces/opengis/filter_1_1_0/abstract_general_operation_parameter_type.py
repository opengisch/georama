from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType
from georama.maps.interfaces.opengis.filter_1_1_0.minimum_occurs import MinimumOccurs

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameterType(DefinitionType):
    """
    Abstract definition of a parameter or group of parameters used by an operation
    method.
    """

    minimum_occurs: MinimumOccurs | None = field(
        default=None,
        metadata={
            "name": "minimumOccurs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
