from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.general_transformation_ref_type import (
    GeneralTransformationRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralTransformationRef(GeneralTransformationRefType):
    class Meta:
        name = "generalTransformationRef"
        namespace = "http://www.opengis.net/gml"
