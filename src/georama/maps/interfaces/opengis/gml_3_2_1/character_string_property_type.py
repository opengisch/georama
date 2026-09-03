from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.character_string import CharacterString
from georama.maps.interfaces.opengis.gml_3_2_1.ci_date_type_code import CiDateTypeCode
from georama.maps.interfaces.opengis.gml_3_2_1.ci_on_line_function_code import (
    CiOnLineFunctionCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_presentation_form_code import (
    CiPresentationFormCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_role_code import CiRoleCode
from georama.maps.interfaces.opengis.gml_3_2_1.country import Country
from georama.maps.interfaces.opengis.gml_3_2_1.dq_evaluation_method_type_code import (
    DqEvaluationMethodTypeCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ds_association_type_code import (
    DsAssociationTypeCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ds_initiative_type_code import (
    DsInitiativeTypeCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.language_code import LanguageCode
from georama.maps.interfaces.opengis.gml_3_2_1.localised_character_string import (
    LocalisedCharacterString,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_cell_geometry_code import (
    MdCellGeometryCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_character_set_code import (
    MdCharacterSetCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_classification_code import (
    MdClassificationCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_coverage_content_type_code import (
    MdCoverageContentTypeCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_datatype_code import MdDatatypeCode
from georama.maps.interfaces.opengis.gml_3_2_1.md_dimension_name_type_code import (
    MdDimensionNameTypeCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_distribution_units import (
    MdDistributionUnits,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_geometric_object_type_code import (
    MdGeometricObjectTypeCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_imaging_condition_code import (
    MdImagingConditionCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_keyword_type_code import (
    MdKeywordTypeCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_maintenance_frequency_code import (
    MdMaintenanceFrequencyCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_medium_format_code import (
    MdMediumFormatCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_medium_name_code import (
    MdMediumNameCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_obligation_code import (
    MdObligationCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_pixel_orientation_code import (
    MdPixelOrientationCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_progress_code import MdProgressCode
from georama.maps.interfaces.opengis.gml_3_2_1.md_restriction_code import (
    MdRestrictionCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_scope_code import MdScopeCode
from georama.maps.interfaces.opengis.gml_3_2_1.md_spatial_representation_type_code import (
    MdSpatialRepresentationTypeCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_topic_category_code import (
    MdTopicCategoryCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_topology_level_code import (
    MdTopologyLevelCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class CharacterStringPropertyType:
    class Meta:
        name = "CharacterString_PropertyType"

    country: Country | None = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    language_code: LanguageCode | None = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    localised_character_string: LocalisedCharacterString | None = field(
        default=None,
        metadata={
            "name": "LocalisedCharacterString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_evaluation_method_type_code: DqEvaluationMethodTypeCode | None = field(
        default=None,
        metadata={
            "name": "DQ_EvaluationMethodTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_initiative_type_code: DsInitiativeTypeCode | None = field(
        default=None,
        metadata={
            "name": "DS_InitiativeTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_association_type_code: DsAssociationTypeCode | None = field(
        default=None,
        metadata={
            "name": "DS_AssociationTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_keyword_type_code: MdKeywordTypeCode | None = field(
        default=None,
        metadata={
            "name": "MD_KeywordTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_progress_code: MdProgressCode | None = field(
        default=None,
        metadata={
            "name": "MD_ProgressCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_spatial_representation_type_code: MdSpatialRepresentationTypeCode | None = field(
        default=None,
        metadata={
            "name": "MD_SpatialRepresentationTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_character_set_code: MdCharacterSetCode | None = field(
        default=None,
        metadata={
            "name": "MD_CharacterSetCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_topic_category_code: MdTopicCategoryCode | None = field(
        default=None,
        metadata={
            "name": "MD_TopicCategoryCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_scope_code: MdScopeCode | None = field(
        default=None,
        metadata={
            "name": "MD_ScopeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_maintenance_frequency_code: MdMaintenanceFrequencyCode | None = field(
        default=None,
        metadata={
            "name": "MD_MaintenanceFrequencyCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_medium_name_code: MdMediumNameCode | None = field(
        default=None,
        metadata={
            "name": "MD_MediumNameCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_medium_format_code: MdMediumFormatCode | None = field(
        default=None,
        metadata={
            "name": "MD_MediumFormatCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_distribution_units: MdDistributionUnits | None = field(
        default=None,
        metadata={
            "name": "MD_DistributionUnits",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_restriction_code: MdRestrictionCode | None = field(
        default=None,
        metadata={
            "name": "MD_RestrictionCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_classification_code: MdClassificationCode | None = field(
        default=None,
        metadata={
            "name": "MD_ClassificationCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_imaging_condition_code: MdImagingConditionCode | None = field(
        default=None,
        metadata={
            "name": "MD_ImagingConditionCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_coverage_content_type_code: MdCoverageContentTypeCode | None = field(
        default=None,
        metadata={
            "name": "MD_CoverageContentTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_datatype_code: MdDatatypeCode | None = field(
        default=None,
        metadata={
            "name": "MD_DatatypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_obligation_code: MdObligationCode | None = field(
        default=None,
        metadata={
            "name": "MD_ObligationCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_dimension_name_type_code: MdDimensionNameTypeCode | None = field(
        default=None,
        metadata={
            "name": "MD_DimensionNameTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_cell_geometry_code: MdCellGeometryCode | None = field(
        default=None,
        metadata={
            "name": "MD_CellGeometryCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_geometric_object_type_code: MdGeometricObjectTypeCode | None = field(
        default=None,
        metadata={
            "name": "MD_GeometricObjectTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_topology_level_code: MdTopologyLevelCode | None = field(
        default=None,
        metadata={
            "name": "MD_TopologyLevelCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_pixel_orientation_code: MdPixelOrientationCode | None = field(
        default=None,
        metadata={
            "name": "MD_PixelOrientationCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ci_date_type_code: CiDateTypeCode | None = field(
        default=None,
        metadata={
            "name": "CI_DateTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ci_on_line_function_code: CiOnLineFunctionCode | None = field(
        default=None,
        metadata={
            "name": "CI_OnLineFunctionCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ci_presentation_form_code: CiPresentationFormCode | None = field(
        default=None,
        metadata={
            "name": "CI_PresentationFormCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ci_role_code: CiRoleCode | None = field(
        default=None,
        metadata={
            "name": "CI_RoleCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    character_string: CharacterString | None = field(
        default=None,
        metadata={
            "name": "CharacterString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
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
