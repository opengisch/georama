from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.dq_element_property_type import (
    DqElementPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.dq_scope_property_type import (
    DqScopePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.li_lineage_property_type import (
    LiLineagePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqDataQualityType(AbstractObjectType):
    class Meta:
        name = "DQ_DataQuality_Type"

    scope: DqScopePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    report: list[DqElementPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    lineage: LiLineagePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
