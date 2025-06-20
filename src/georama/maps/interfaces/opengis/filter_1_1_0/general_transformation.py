from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_transformation_type import (
    AbstractGeneralTransformationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralTransformation(AbstractGeneralTransformationType):
    class Meta:
        name = "_GeneralTransformation"
        namespace = "http://www.opengis.net/gml"
