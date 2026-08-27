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
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
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
    code: CharacterStringPropertyType | None = field(
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

    code_space: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    version: CharacterStringPropertyType | None = field(
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

    rs_identifier: RsIdentifier | None = field(
        default=None,
        metadata={
            "name": "RS_Identifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_identifier: MdIdentifier | None = field(
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
            "min_length": 1,
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateType | None = field(
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
class CiCitationType(AbstractObjectType):
    """
    Standardized resource reference.
    """

    class Meta:
        name = "CI_Citation_Type"

    title: CharacterStringPropertyType | None = field(
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
    edition: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    edition_date: DatePropertyType | None = field(
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
    series: CiSeriesPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    other_citation_details: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "otherCitationDetails",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    collective_title: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "collectiveTitle",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    isbn: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    issn: CharacterStringPropertyType | None = field(
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

    ci_citation: CiCitation | None = field(
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
            "min_length": 1,
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateType | None = field(
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
