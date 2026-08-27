from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.integer_property_type import (
    IntegerPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_dimension_name_type_code_property_type import (
    MdDimensionNameTypeCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.measure_property_type import (
    MeasurePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDimensionType(AbstractObjectType):
    class Meta:
        name = "MD_Dimension_Type"

    dimension_name: MdDimensionNameTypeCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "dimensionName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    dimension_size: IntegerPropertyType | None = field(
        default=None,
        metadata={
            "name": "dimensionSize",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    resolution: MeasurePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
