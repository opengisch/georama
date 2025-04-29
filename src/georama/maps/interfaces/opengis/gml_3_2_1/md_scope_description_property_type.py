from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_scope_description import (
    MdScopeDescription,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdScopeDescriptionPropertyType:
    class Meta:
        name = "MD_ScopeDescription_PropertyType"

    md_scope_description: Optional[MdScopeDescription] = field(
        default=None,
        metadata={
            "name": "MD_ScopeDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
