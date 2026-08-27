from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_md_content_information_type import (
    AbstractMdContentInformationType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_coverage_content_type_code_property_type import (
    MdCoverageContentTypeCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_range_dimension_property_type import (
    MdRangeDimensionPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.record_type_property_type import (
    RecordTypePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdCoverageDescriptionType(AbstractMdContentInformationType):
    """
    Information about the domain of the raster cell.
    """

    class Meta:
        name = "MD_CoverageDescription_Type"

    attribute_description: RecordTypePropertyType | None = field(
        default=None,
        metadata={
            "name": "attributeDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    content_type: MdCoverageContentTypeCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    dimension: list[MdRangeDimensionPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
