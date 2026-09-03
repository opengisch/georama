from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ex_extent_property_type import (
    ExExtentPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.rs_identifier_property_type import (
    RsIdentifierPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractRsReferenceSystemType(AbstractObjectType):
    """
    Description of the spatial and temporal reference systems used in the dataset.
    """

    class Meta:
        name = "AbstractRS_ReferenceSystem_Type"

    name: RsIdentifierPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    domain_of_validity: list[ExExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
