from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_topic_category_code import (
    MdTopicCategoryCode,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdTopicCategoryCodePropertyType:
    class Meta:
        name = "MD_TopicCategoryCode_PropertyType"

    md_topic_category_code: Optional[MdTopicCategoryCode] = field(
        default=None,
        metadata={
            "name": "MD_TopicCategoryCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
