from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.md_topic_category_code_type import (
    MdTopicCategoryCodeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdTopicCategoryCode:
    class Meta:
        name = "MD_TopicCategoryCode"
        namespace = "http://www.isotc211.org/2005/gmd"

    value: MdTopicCategoryCodeType | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
