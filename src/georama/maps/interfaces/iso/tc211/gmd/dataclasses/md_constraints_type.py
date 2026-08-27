from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdConstraintsType(AbstractObjectType):
    """
    Restrictions on the access and use of a dataset or metadata.
    """

    class Meta:
        name = "MD_Constraints_Type"

    use_limitation: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "useLimitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
