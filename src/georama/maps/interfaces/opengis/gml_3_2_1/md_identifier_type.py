from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_date_property_type import (
    CiDatePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_presentation_form_code_property_type import (
    CiPresentationFormCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_series_property_type import (
    CiSeriesPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.date_property_type import (
    DatePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdIdentifierType(AbstractObjectType):
    class Meta:
        name = "MD_Identifier_Type"

    authority: Optional["CiCitationPropertyType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    code: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )


@dataclass
class MdIdentifier(MdIdentifierType):
    class Meta:
        name = "MD_Identifier"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class RsIdentifierType(MdIdentifierType):
    class Meta:
        name = "RS_Identifier_Type"

    code_space: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    version: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class RsIdentifier(RsIdentifierType):
    class Meta:
        name = "RS_Identifier"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdIdentifierPropertyType:
    class Meta:
        name = "MD_Identifier_PropertyType"

    rs_identifier: Optional[RsIdentifier] = field(
        default=None,
        metadata={
            "name": "RS_Identifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_identifier: Optional[MdIdentifier] = field(
        default=None,
        metadata={
            "name": "MD_Identifier",
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
class CiCitationType(AbstractObjectType):
    """
    Standardized resource reference.
    """

    class Meta:
        name = "CI_Citation_Type"

    title: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    alternate_title: list[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "alternateTitle",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    date: list[CiDatePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    edition: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    edition_date: Optional[DatePropertyType] = field(
        default=None,
        metadata={
            "name": "editionDate",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    identifier: list[MdIdentifierPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    cited_responsible_party: list[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "citedResponsibleParty",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    presentation_form: list[CiPresentationFormCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "presentationForm",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    series: Optional[CiSeriesPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    other_citation_details: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "otherCitationDetails",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    collective_title: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "collectiveTitle",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    isbn: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    issn: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "ISSN",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class CiCitation(CiCitationType):
    class Meta:
        name = "CI_Citation"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiCitationPropertyType:
    class Meta:
        name = "CI_Citation_PropertyType"

    ci_citation: Optional[CiCitation] = field(
        default=None,
        metadata={
            "name": "CI_Citation",
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
