from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.local_name import LocalName
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.scoped_name import ScopedName

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class GenericNamePropertyType:
    class Meta:
        name = "GenericName_PropertyType"

    scoped_name: Optional[ScopedName] = field(
        default=None,
        metadata={
            "name": "ScopedName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    local_name: Optional[LocalName] = field(
        default=None,
        metadata={
            "name": "LocalName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
