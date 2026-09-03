from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.li_process_step_type import (
    LiProcessStepPropertyType,
    LiSourcePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiLineageType(AbstractObjectType):
    class Meta:
        name = "LI_Lineage_Type"

    statement: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    process_step: list[LiProcessStepPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "processStep",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source: list[LiSourcePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
