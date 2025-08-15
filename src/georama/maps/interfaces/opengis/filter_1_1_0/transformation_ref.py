from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.transformation_ref_type import (
    TransformationRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TransformationRef(TransformationRefType):
    class Meta:
        name = "transformationRef"
        namespace = "http://www.opengis.net/gml"
