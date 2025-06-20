from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.transformation_type import (
    TransformationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Transformation(TransformationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
