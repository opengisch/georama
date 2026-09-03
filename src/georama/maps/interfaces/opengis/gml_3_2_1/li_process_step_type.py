from dataclasses import dataclass, field

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
from georama.maps.interfaces.opengis.gml_3_2_1.date_time_property_type import (
    DateTimePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ex_extent_property_type import (
    ExExtentPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_identifier_type import (
    CiCitationPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_reference_system_property_type import (
    MdReferenceSystemPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_representative_fraction_property_type import (
    MdRepresentativeFractionPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiProcessStepType(AbstractObjectType):
    class Meta:
        name = "LI_ProcessStep_Type"

    description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    rationale: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    date_time: DateTimePropertyType | None = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    processor: list[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source: list["LiSourcePropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class LiProcessStep(LiProcessStepType):
    class Meta:
        name = "LI_ProcessStep"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiProcessStepPropertyType:
    class Meta:
        name = "LI_ProcessStep_PropertyType"

    li_process_step: LiProcessStep | None = field(
        default=None,
        metadata={
            "name": "LI_ProcessStep",
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
class LiSourceType(AbstractObjectType):
    class Meta:
        name = "LI_Source_Type"

    description: CharacterStringPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    scale_denominator: MdRepresentativeFractionPropertyType | None = field(
        default=None,
        metadata={
            "name": "scaleDenominator",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source_reference_system: MdReferenceSystemPropertyType | None = field(
        default=None,
        metadata={
            "name": "sourceReferenceSystem",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source_citation: CiCitationPropertyType | None = field(
        default=None,
        metadata={
            "name": "sourceCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source_extent: list[ExExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "sourceExtent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source_step: list[LiProcessStepPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "sourceStep",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class LiSource(LiSourceType):
    class Meta:
        name = "LI_Source"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiSourcePropertyType:
    class Meta:
        name = "LI_Source_PropertyType"

    li_source: LiSource | None = field(
        default=None,
        metadata={
            "name": "LI_Source",
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
