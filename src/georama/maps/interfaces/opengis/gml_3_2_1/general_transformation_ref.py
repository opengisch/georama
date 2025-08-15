from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.general_transformation_property_type import (
    GeneralTransformationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeneralTransformationRef(GeneralTransformationPropertyType):
    class Meta:
        name = "generalTransformationRef"
        namespace = "http://www.opengis.net/gml/3.2"
