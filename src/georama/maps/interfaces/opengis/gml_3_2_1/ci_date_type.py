from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ci_date_type_code_property_type import (
    CiDateTypeCodePropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.date_property_type import (
    DatePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiDateType(AbstractObjectType):
    class Meta:
        name = "CI_Date_Type"

    date: DatePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    date_type: CiDateTypeCodePropertyType | None = field(
        default=None,
        metadata={
            "name": "dateType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
