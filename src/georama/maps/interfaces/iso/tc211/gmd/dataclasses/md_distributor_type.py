from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_digital_transfer_options_property_type import (
    MdDigitalTransferOptionsPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_standard_order_process_property_type import (
    MdStandardOrderProcessPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributorType(AbstractObjectType):
    """
    Information about the distributor.
    """

    class Meta:
        name = "MD_Distributor_Type"

    distributor_contact: CiResponsiblePartyPropertyType | None = field(
        default=None,
        metadata={
            "name": "distributorContact",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    distribution_order_process: list[MdStandardOrderProcessPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "distributionOrderProcess",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    distributor_format: list["MdFormatPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "distributorFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    distributor_transfer_options: list[MdDigitalTransferOptionsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "distributorTransferOptions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class MdDistributor(MdDistributorType):
    class Meta:
        name = "MD_Distributor"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributorPropertyType:
    class Meta:
        name = "MD_Distributor_PropertyType"

    md_distributor: MdDistributor | None = field(
        default=None,
        metadata={
            "name": "MD_Distributor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: str = field(
        init=False,
        default="simple",
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    uuidref: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )


@dataclass
class MdFormatType(AbstractObjectType):
    """
    Description of the form of the data to be distributed.
    """

    class Meta:
        name = "MD_Format_Type"

    name: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    version: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    amendment_number: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "amendmentNumber",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    specification: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    file_decompression_technique: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "fileDecompressionTechnique",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    format_distributor: list[MdDistributorPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "formatDistributor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class MdFormat(MdFormatType):
    class Meta:
        name = "MD_Format"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdFormatPropertyType:
    class Meta:
        name = "MD_Format_PropertyType"

    md_format: MdFormat | None = field(
        default=None,
        metadata={
            "name": "MD_Format",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: str = field(
        init=False,
        default="simple",
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    uuidref: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
