from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.rs_identifier_property_type import (
    RsIdentifierPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdReferenceSystemType(AbstractObjectType):
    class Meta:
        name = "MD_ReferenceSystem_Type"

    reference_system_identifier: Optional[RsIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "referenceSystemIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
