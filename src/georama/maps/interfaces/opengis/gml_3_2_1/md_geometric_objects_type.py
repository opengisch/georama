from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.integer_property_type import (
    IntegerPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.md_geometric_object_type_code_property_type import (
    MdGeometricObjectTypeCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeometricObjectsType(AbstractObjectType):
    class Meta:
        name = "MD_GeometricObjects_Type"

    geometric_object_type: MdGeometricObjectTypeCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "geometricObjectType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    geometric_object_count: IntegerPropertyType | None = field(
        default=None,
        metadata={
            "name": "geometricObjectCount",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
