from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.local_name import LocalName

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class LocalNamePropertyType:
    class Meta:
        name = "LocalName_PropertyType"

    local_name: Optional[LocalName] = field(
        default=None,
        metadata={
            "name": "LocalName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
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
