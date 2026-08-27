from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.tm_primitive_property_type import (
    TmPrimitivePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExTemporalExtentType(AbstractObjectType):
    """
    Time period covered by the content of the dataset.
    """

    class Meta:
        name = "EX_TemporalExtent_Type"

    extent: TmPrimitivePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
