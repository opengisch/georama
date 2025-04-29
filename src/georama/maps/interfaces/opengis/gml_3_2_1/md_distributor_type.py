from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_digital_transfer_options_property_type import (
    MdDigitalTransferOptionsPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_standard_order_process_property_type import (
    MdStandardOrderProcessPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributorType(AbstractObjectType):
    """
    Information about the distributor.
    """

    class Meta:
        name = "MD_Distributor_Type"

    distributor_contact: Optional[CiResponsiblePartyPropertyType] = field(
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

    md_distributor: Optional[MdDistributor] = field(
        default=None,
        metadata={
            "name": "MD_Distributor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


@dataclass
class MdFormatType(AbstractObjectType):
    """
    Description of the form of the data to be distributed.
    """

    class Meta:
        name = "MD_Format_Type"

    name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    version: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    amendment_number: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "amendmentNumber",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    specification: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    file_decompression_technique: Optional[CharacterStringPropertyType] = field(
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

    md_format: Optional[MdFormat] = field(
        default=None,
        metadata={
            "name": "MD_Format",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
