from dataclasses import dataclass, field
from typing import List, Optional, Union

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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.date_property_type import (
    DatePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_data_quality_property_type import (
    DqDataQualityPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_application_schema_information_property_type import (
    MdApplicationSchemaInformationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_character_set_code_property_type import (
    MdCharacterSetCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_constraints_property_type import (
    MdConstraintsPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_content_information_property_type import (
    MdContentInformationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_distribution_property_type import (
    MdDistributionPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_identification_property_type import (
    MdIdentificationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_maintenance_information_property_type import (
    MdMaintenanceInformationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_metadata_extension_information_property_type import (
    MdMetadataExtensionInformationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_portrayal_catalogue_reference_property_type import (
    MdPortrayalCatalogueReferencePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_reference_system_property_type import (
    MdReferenceSystemPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_scope_code_property_type import (
    MdScopeCodePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_spatial_representation_property_type import (
    MdSpatialRepresentationPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.object_reference_property_type import (
    ObjectReferencePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pt_locale_property_type import (
    PtLocalePropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMetadataType(AbstractObjectType):
    """
    Information about the metadata.
    """

    class Meta:
        name = "MD_Metadata_Type"

    file_identifier: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "fileIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    language: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    character_set: Optional[MdCharacterSetCodePropertyType] = field(
        default=None,
        metadata={
            "name": "characterSet",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    parent_identifier: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "parentIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    hierarchy_level: List[MdScopeCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "hierarchyLevel",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    hierarchy_level_name: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "hierarchyLevelName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    contact: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    date_stamp: Optional[DatePropertyType] = field(
        default=None,
        metadata={
            "name": "dateStamp",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    metadata_standard_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "metadataStandardName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    metadata_standard_version: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "metadataStandardVersion",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    data_set_uri: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "dataSetURI",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    locale: List[PtLocalePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    spatial_representation_info: List[MdSpatialRepresentationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialRepresentationInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    reference_system_info: List[MdReferenceSystemPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "referenceSystemInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    metadata_extension_info: List[MdMetadataExtensionInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "metadataExtensionInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    identification_info: List[MdIdentificationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "identificationInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    content_info: List[MdContentInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "contentInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    distribution_info: Optional[MdDistributionPropertyType] = field(
        default=None,
        metadata={
            "name": "distributionInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    data_quality_info: List[DqDataQualityPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "dataQualityInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    portrayal_catalogue_info: List[MdPortrayalCatalogueReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "portrayalCatalogueInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    metadata_constraints: List[MdConstraintsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "metadataConstraints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    application_schema_info: List[MdApplicationSchemaInformationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "applicationSchemaInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    metadata_maintenance: Optional[MdMaintenanceInformationPropertyType] = field(
        default=None,
        metadata={
            "name": "metadataMaintenance",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    series: List["DsAggregatePropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    describes: List["DsDataSetPropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    property_type: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "propertyType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    feature_type: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    feature_attribute: List[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureAttribute",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class MdMetadata(MdMetadataType):
    class Meta:
        name = "MD_Metadata"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMetadataPropertyType:
    class Meta:
        name = "MD_Metadata_PropertyType"

    md_metadata: Optional[MdMetadata] = field(
        default=None,
        metadata={
            "name": "MD_Metadata",
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
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
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
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )


@dataclass
class AbstractDsAggregateType(AbstractObjectType):
    """
    Identifiable collection of datasets.
    """

    class Meta:
        name = "AbstractDS_Aggregate_Type"

    composed_of: List["DsDataSetPropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "composedOf",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    series_metadata: List[MdMetadataPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "seriesMetadata",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    subset: List["DsAggregatePropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    superset: List["DsAggregatePropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class DsInitiativeType(AbstractDsAggregateType):
    class Meta:
        name = "DS_Initiative_Type"


@dataclass
class DsOtherAggregateType(AbstractDsAggregateType):
    class Meta:
        name = "DS_OtherAggregate_Type"


@dataclass
class DsSeriesType(AbstractDsAggregateType):
    class Meta:
        name = "DS_Series_Type"


@dataclass
class DsInitiative(DsInitiativeType):
    class Meta:
        name = "DS_Initiative"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsOtherAggregate(DsOtherAggregateType):
    class Meta:
        name = "DS_OtherAggregate"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsPlatformType(DsSeriesType):
    class Meta:
        name = "DS_Platform_Type"


@dataclass
class DsProductionSeriesType(DsSeriesType):
    class Meta:
        name = "DS_ProductionSeries_Type"


@dataclass
class DsSensorType(DsSeriesType):
    class Meta:
        name = "DS_Sensor_Type"


@dataclass
class DsSeries(DsSeriesType):
    class Meta:
        name = "DS_Series"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsStereoMateType(DsOtherAggregateType):
    class Meta:
        name = "DS_StereoMate_Type"


@dataclass
class DsPlatform(DsPlatformType):
    class Meta:
        name = "DS_Platform"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsProductionSeries(DsProductionSeriesType):
    class Meta:
        name = "DS_ProductionSeries"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsSensor(DsSensorType):
    class Meta:
        name = "DS_Sensor"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsStereoMate(DsStereoMateType):
    class Meta:
        name = "DS_StereoMate"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsAggregatePropertyType:
    class Meta:
        name = "DS_Aggregate_PropertyType"

    ds_initiative: Optional[DsInitiative] = field(
        default=None,
        metadata={
            "name": "DS_Initiative",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_production_series: Optional[DsProductionSeries] = field(
        default=None,
        metadata={
            "name": "DS_ProductionSeries",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_sensor: Optional[DsSensor] = field(
        default=None,
        metadata={
            "name": "DS_Sensor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_platform: Optional[DsPlatform] = field(
        default=None,
        metadata={
            "name": "DS_Platform",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_series: Optional[DsSeries] = field(
        default=None,
        metadata={
            "name": "DS_Series",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_stereo_mate: Optional[DsStereoMate] = field(
        default=None,
        metadata={
            "name": "DS_StereoMate",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_other_aggregate: Optional[DsOtherAggregate] = field(
        default=None,
        metadata={
            "name": "DS_OtherAggregate",
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
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
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
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )


@dataclass
class DsDataSetType(AbstractObjectType):
    """
    Identifiable collection of data.
    """

    class Meta:
        name = "DS_DataSet_Type"

    has: List[MdMetadataPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    part_of: List[DsAggregatePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "partOf",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class DsDataSet(DsDataSetType):
    class Meta:
        name = "DS_DataSet"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsDataSetPropertyType:
    class Meta:
        name = "DS_DataSet_PropertyType"

    ds_data_set: Optional[DsDataSet] = field(
        default=None,
        metadata={
            "name": "DS_DataSet",
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
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
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
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
