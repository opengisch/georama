from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ex_extent_property_type import (
    ExExtentPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_scope_code_property_type import (
    MdScopeCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_scope_description_property_type import (
    MdScopeDescriptionPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqScopeType(AbstractObjectType):
    class Meta:
        name = "DQ_Scope_Type"

    level: Optional[MdScopeCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    extent: Optional[ExExtentPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    level_description: List[MdScopeDescriptionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "levelDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
